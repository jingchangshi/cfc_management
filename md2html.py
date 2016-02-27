import os, sys

# import subprocess

InputFilePathStr = os.path.abspath(sys.argv[1])
InputFormatStr = "markdown"
OutputFormatStr = "html"
ArgTemplateStr = "--template=./Html.template"
InputFileName, InputFileExtension = os.path.splitext(InputFilePathStr)
OutputFilePathStr = InputFileName + "." + OutputFormatStr
ArgNumSecStr = "--number-sections"
ArgNumSecOffStr = "--number-offset=0"
SystemCmdList = \
	["pandoc", "-f", InputFormatStr, "-t", OutputFormatStr, \
	ArgTemplateStr, ArgNumSecStr, ArgNumSecOffStr, \
	"\""+InputFilePathStr+"\"", "-o", "\""+OutputFilePathStr+"\""]
SystemCmdStr = " ".join(SystemCmdList)
os.system(SystemCmdStr)