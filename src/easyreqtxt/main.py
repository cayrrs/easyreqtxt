import importlib.metadata
import ast
import logging
import sys
from pathlib import Path
import argparse

package_map = importlib.metadata.packages_distributions()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


modules = []


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scan a folder for Python imports and resolve their versions, and output them to a requirements.txt"
    )
    parser.add_argument(
        "folder",
        type=str,
        help="Path to the folder to scan."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="requirements.txt",
        help="Output filename (default: requirements.txt)"
    )
    return parser.parse_args()



def walkfile(filepath: Path):
    filename = filepath.name
    module_names = []
    logger.info(f"Beginning walk on {filename}")
    with open(filepath, 'r',encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source)
    walk = (ast.walk(tree))
    for node in walk:
        if isinstance(node, ast.Import):
            for alias in node.names:
                nm = alias.name.split(".")[0]
                if nm in module_names:
                    continue
                module_names.append(nm)
                logger.info(f"Found {nm} in {filename}")
        else:
            if isinstance(node, ast.ImportFrom):
                if node.level > 0 or node.module is None:
                    continue
                name = node.module.split(".")[0]
                if name in module_names:
                    continue
                module_names.append(name)
                logger.info(f"Found {name} in {filename}")
                
    logger.info(f"Finished dependency walk on {filename}!")
    logger.info(f"Beginning dist name corrections")
    for module in module_names:
        if module in sys.stdlib_module_names:
            logger.info(f"Skipping baselib module: {module}")
            continue
        if module in package_map:
            distnames = package_map[module]
            if len(distnames) > 1:
                logger.warning(f"Module {module} maps to multiple packages. I shall use the first one.")
            distname = distnames[0]
            logger.debug(f"{module} -> {distname}")
            if any(distname in m for m in modules):
                logger.info(f"Skipping repeated module: {distname}")
                continue
            try:
                version = importlib.metadata.version(distname)
            except importlib.metadata.PackageNotFoundError as e:
                logging.warning(f"Unable to obtain a version for module {module}. Reason: {e}")
                version = None
            
            modules.append({distname: version})
        else:
            if any(module in m for m in modules):
                logger.info(f"Skipping repeated module: {module}")
                continue
            try:
                version = importlib.metadata.version(module)
            except importlib.metadata.PackageNotFoundError as e:
                logging.warning(f"Unable to obtain a version for module {module}. Reason: {e}. Version number will equal None. This can happen if the module isn't installed.")
                version = None
            modules.append({module: version})
    
    logger.info(f"Walk of file {filename} finished!")

            
    
def output(filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        for m in modules:
            for name, ver in m.items():
                if ver == None:
                    string = f"{name}"
                else:
                    string = f"{name}=={ver}"
                f.write(string + "\n")
    logger.info(f"Outputted depedency list at {filename}")

            
def main():
    args = parse_args()
    for f in Path(args.folder).rglob("*.py"):
        walkfile(f)
    output(args.output)


if __name__ == "__main__":
    main()

    

