with open("/mnt/code/job_file.txt", "w+") as code_file:
    code_file.write("file in code")
with open("/mnt/artifacts/job_file.txt", "w+") as artifact_file:
    artifact_file.write("file in artifacts")   
