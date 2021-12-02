import numpy as np
import cv2

imdata = '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GDzDomIk6F862mJ+8E03F0Z5nclFmuRkK5Kde8HmqyJ4ATH+FOweWRCRAAAPVGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNC40LjAtRXhpdjIiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6aXB0Y0V4dD0iaHR0cDovL2lwdGMub3JnL3N0ZC9JcHRjNHhtcEV4dC8yMDA4LTAyLTI5LyIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgIHhtbG5zOnBsdXM9Imh0dHA6Ly9ucy51c2VwbHVzLm9yZy9sZGYveG1wLzEuMC8iCiAgICB4bWxuczpHSU1QPSJodHRwOi8vd3d3LmdpbXAub3JnL3htcC8iCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgIHhtcE1NOkRvY3VtZW50SUQ9ImdpbXA6ZG9jaWQ6Z2ltcDphMGRlNjBiNS03MjY4LTRkYjItYTU0Mi00OWFiNjg1YmUzNjIiCiAgIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NWVlYTYxZWUtMDczMS00MmEyLWJjNTktYzkyZmI4ZDkwOGM4IgogICB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6MjdlMTBhMTAtMWQ1MC00MzdkLWJhNmMtNTEwMzIzNzEwZGFhIgogICBHSU1QOkFQST0iMi4wIgogICBHSU1QOlBsYXRmb3JtPSJXaW5kb3dzIgogICBHSU1QOlRpbWVTdGFtcD0iMTYxNTE5NTYwMTYxNzE0OCIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjgiCiAgIGRjOkZvcm1hdD0iaW1hZ2UvcG5nIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCI+CiAgIDxpcHRjRXh0OkxvY2F0aW9uQ3JlYXRlZD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkxvY2F0aW9uQ3JlYXRlZD4KICAgPGlwdGNFeHQ6TG9jYXRpb25TaG93bj4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkxvY2F0aW9uU2hvd24+CiAgIDxpcHRjRXh0OkFydHdvcmtPck9iamVjdD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkFydHdvcmtPck9iamVjdD4KICAgPGlwdGNFeHQ6UmVnaXN0cnlJZD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OlJlZ2lzdHJ5SWQ+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmE2NjEyMzgzLWIzZGYtNDBmNS04NTFlLWUzOTY3NjYwMzA0MCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAyMS0wMy0wOFQwOToyNjo0MSIvPgogICAgPC9yZGY6U2VxPgogICA8L3htcE1NOkhpc3Rvcnk+CiAgIDxwbHVzOkltYWdlU3VwcGxpZXI+CiAgICA8cmRmOlNlcS8+CiAgIDwvcGx1czpJbWFnZVN1cHBsaWVyPgogICA8cGx1czpJbWFnZUNyZWF0b3I+CiAgICA8cmRmOlNlcS8+CiAgIDwvcGx1czpJbWFnZUNyZWF0b3I+CiAgIDxwbHVzOkNvcHlyaWdodE93bmVyPgogICAgPHJkZjpTZXEvPgogICA8L3BsdXM6Q29weXJpZ2h0T3duZXI+CiAgIDxwbHVzOkxpY2Vuc29yPgogICAgPHJkZjpTZXEvPgogICA8L3BsdXM6TGljZW5zb3I+CiAgPC9yZGY6RGVzY3JpcHRpb24+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz77oDXnAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5QMICRop9QcrlgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAACAASURBVHja7b15mF1Vne/9WXvvs8881XCqKlWZKgMJISFMgSBgVEAg0oI2oqiobctzu/X1dtt9X1+v96G99vW1Wy9qd2NrS19ofcWrYGM7gA00GIZAMEAIkJlUZajx1HDOqTPvab1/nFPDSaoyGTBc1ud5dlJnn73XXnsN3/1bv/Vb+whAolAoFG8CNFUECoVCCZZCoVAowVIoFEqwFAqFQgmWQqFQKMFSKBRKsBQKhUIJlkKhUCjBUigUSrAUCoVCCZZCoVAowVIoFEqwFAqFQgmWQqFQKMFSKBRKsBQKhUIJlkKhUCjBUigUSrAUCoVCCZZCoVAowVIoFEqwFAqFQgmWQqFQKMFSKBRKsBQKhUIJlkKhUNQxTkciT55/IU0v7UNIA/CBNEFM/u0DfMhIAKcrxkTcz1CuQK9dZltpjKfH+uizSm/oTa+Onc/FsSs4J3Ih87WzSIY7CIokMh3AFlBuq5KVOcay46TNfvorPfSV93CgvI39mRewvfxbsrFEF3YjL9tAMZlAGgJ00D2HSE8Pxcd/g5MvqB71RteJX2PDuQmWpTII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'

imgNp=np.array(bytearray(imdata),dtype=np.uint8)
imgNp = np.transpose(cv2.imdecode(imgNp,-1), (1,0,2))

import matplotlib.pyplot as plt

plt.imshow(imgNp)
plt.show()
