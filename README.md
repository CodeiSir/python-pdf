# Python PDF

## Merge PDF

The script `mergepdf.py` will merge all PDF-files within the current working directory into a new PDF with the same name as the directory.

| Argument | Description                                |
| -------- | ------------------------------------------ |
| `-d`     | source and target directory                |
| `-f`     | output file name without path or extension |

### Install as Linux command

- `nano /etc/bash.bashrc` (Ubuntu)
- Insert new line: `alias mergepdf='python /PATH/mergepdf.py'`
- Example usage: `mergepdf -d /ANOTHER_PATH/ -f 'NEW FILE NAME'`
