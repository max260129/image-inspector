import argparse
import sys
import subprocess
import re

class CustomHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def map_image(image_path):

    lat = ""
    lon = ""

    command = ["exiftool", image_path]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, _ = process.communicate()
    output = output.decode('utf-8')
    
    lines = output.split('\n')
    for line in lines:
        if "GPS Latitude" in line or "GPS Longitude" in line:
            if "Created" not in line and "Ref" not in line:
                if "Latitude" in line:
                    parts = line.split(":")
                    lat = parts[1].split()[0]
                if "Longitude" in line:
                    part = line.split(":")
                    lon = part[1].split()[0]

    result = "Lat/Lon:    " + "(" + lat + ") / (" + lon + ")"
    return result

def steg_image(image_path):
    command = ["strings", image_path]
    res = subprocess.run(command, capture_output=True, text=True)
    res_text = res.stdout

    # Search for text between two "Enter" words
    pattern = re.compile(r"(?<=Enter)(.*?)(?=Enter)", re.DOTALL)
    match = re.search(pattern, res_text)
    if match:
        result = match.group(1).strip()  # Use .strip() to remove leading/trailing whitespace
    else:
        result = ""

    return result


def main():
    parser = CustomHelpParser(add_help=False)
    parser.add_argument('-map', type=str, metavar='IMAGE', help='Mapper l\'image')
    parser.add_argument('-steg', type=str, metavar='IMAGE', help='Appliquer la stéganographie à l\'image')

    args = parser.parse_args()

    if args.map:
        results = map_image(args.map)
        print(results)
    elif args.steg:
        results = steg_image(args.steg)
        print(results)

if __name__ == "__main__":
    main()
