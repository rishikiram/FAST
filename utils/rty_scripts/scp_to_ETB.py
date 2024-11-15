import os
import paramiko
from tqdm import tqdm
DATA_DIR = "/Users/rishi/envitrace repos/SeisDetection/data"
ETB_DIR = "C:/Users/risht/Downloads/UUFORK"

def main():
    for filename in tqdm(os.listdir(DATA_DIR)):
        file_path = os.path.join(DATA_DIR, filename)
        assert(os.path.isfile(file_path))

        remote_path = os.path.join(ETB_DIR, filename)
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join("/Users/rishi", ".ssh", "known_hosts")))
        try:
            ssh.connect("98.60.118.144", username="risht", password="E^Al2aIz3Jo3", port=8901)
            sftp = ssh.open_sftp()
            # sftp.chdir(ETB_DIR)
            try:
                print(sftp.stat(remote_path))
                print(filename+' already exists')
            except IOError:
                sftp.put(file_path, remote_path)
            sftp.close()
            ssh.close()
        except paramiko.SSHException:
            print("Connection Error")

# old
    # ssh.connect("98.60.118.144", username="risht", password="E^Al2aIz3Jo3", port=8901)
    # sftp = ssh.open_sftp()
    # sftp.put(file_path, remote_path)
    # sftp.close()
    # ssh.close()

if __name__ == "__main__":
    main()