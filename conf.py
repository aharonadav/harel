#!/usr/bin/env python
import tarfile
import shutil
import os
import sys
import MySQLdb as mysql


# old_stdout = sys.stdout
# log_file = open("./os-details.txt", "a")
# sys.stdout = log_file

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

buildnambuer = os.environ['BUILD_NUMBER']
builname = os.environ['BUILD_DISPLAY_NAME']
workspace = os.environ['WORKSPACE']
gitbranch = os.environ['GIT_BRANCH'].split("/")[1]
gitrepository = os.environ['GIT_URL'].split("/")[4].split(".")[0]


print gitrepository
print gitbranch

#DB connection
cnx = mysql.connect("prod_gitlab",      # your host, usually localhost
                    "root",             # your username
                    "gitlab_deploy")    # name of the data base

cur = cnx.cursor()

#Get the data from the DB
query = "SELECT working_dir, git_dir, destination_hosts, deployment_path, exclude_file FROM gitlab_deploy.repository_branch_data WHERE repository = '%s' AND branch_name = '%s'" % \
        (gitrepository, gitbranch)

cur.execute(query)

data = cur.fetchone()

#define query results into variables
workDir, gitDir, destHost, deployPath, exclude_file = data[0:6]
destHosts = destHost.split(",")

print "\n%s\n%s\n%s\n%s\n%s " % \
            (workDir, gitDir, destHost, deployPath, exclude_file)  
for host in destHosts:
    print "\n%s" % host

if len(destHosts) > 1:
    for host in destHosts:
        rsync = "sudo rsync --delete --exclude-from '%s' -avz -e 'ssh -i /master.pem' %s/ root@%s:%s" % \
                (exclude_file, workspace, host, deployPath)
        chown = "sudo ssh -i '/master.pem' root@%s 'chown -R nginx:nginx %s'" % (host, deployPath)
        #grunt = "sudo ssh -i '/master.pem' root@%s 'cd %s && grunt'" % (host, deployPath)
        os.system(rsync)
        os.system(chown)
        #os.system(grunt)
        #Running npm run bundle on deployPath
       	#bundle = "sudo ssh -i '/master.pem' root@%s 'cd %s && npm run bundle'" % (host, deployPath)
        #os.system(bundle)
        #print(bundle)
else:
    rsync = "sudo rsync --delete --exclude-from '%s' -avz -e 'ssh -i /master.pem' %s/ root@%s:%s" % \
                (exclude_file, workspace, destHost, deployPath)
    chown = "sudo ssh -i '/master.pem' root@%s 'chown -R nginx:nginx %s'" % (destHost, deployPath)
    #grunt = "sudo ssh -i '/master.pem' root@%s 'cd %s && grunt'" % (destHost, deployPath)
    os.system(rsync)
    os.system(chown)
    #os.system(grunt)
    #Running npm run bundle on deployPath
    #bundle = "sudo ssh -i '/master.pem' root@%s 'cd %s && npm run bundle'" % (destHost, deployPath)
    #os.system(bundle)
    #print(bundle)

    
#bundle = "sudo ssh -i '/master.pem' root@prod_hdgs_web1 'cd %s && npm run bundle'" % (deployPath)
#os.system(bundle)
#print(bundle) 

#make_tarfile(builname+"_"+buildnambuer+".tar.gz", workspace)
#shutil.move(builname+"_"+buildnambuer+".tar.gz", '/opt/builds_tar/')

#Closing log file
# sys.stdout = old_stdout
# log_file.close()
cnx.close()
exit(0)#!/usr/bin/env python
import tarfile
import shutil
import os
import sys
import MySQLdb as mysql


# old_stdout = sys.stdout
# log_file = open("./os-details.txt", "a")
# sys.stdout = log_file

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

buildnambuer = os.environ['BUILD_NUMBER']
builname = os.environ['BUILD_DISPLAY_NAME']
workspace = os.environ['WORKSPACE']
gitbranch = os.environ['GIT_BRANCH'].split("/")[1]
gitrepository = os.environ['GIT_URL'].split("/")[4].split(".")[0]


print gitrepository
print gitbranch

#DB connection
cnx = mysql.connect("prod_gitlab",      # your host, usually localhost
                    "root",             # your username
                    "gitlab_deploy")    # name of the data base

cur = cnx.cursor()

#Get the data from the DB
query = "SELECT working_dir, git_dir, destination_hosts, deployment_path, exclude_file FROM gitlab_deploy.repository_branch_data WHERE repository = '%s' AND branch_name = '%s'" % \
        (gitrepository, gitbranch)

cur.execute(query)

data = cur.fetchone()

#define query results into variables
workDir, gitDir, destHost, deployPath, exclude_file = data[0:6]
destHosts = destHost.split(",")

print "\n%s\n%s\n%s\n%s\n%s " % \
            (workDir, gitDir, destHost, deployPath, exclude_file)  
for host in destHosts:
    print "\n%s" % host

if len(destHosts) > 1:
    for host in destHosts:
        rsync = "sudo rsync --delete --exclude-from '%s' -avz -e 'ssh -i /master.pem' %s/ root@%s:%s" % \
                (exclude_file, workspace, host, deployPath)
        chown = "sudo ssh -i '/master.pem' root@%s 'chown -R nginx:nginx %s'" % (host, deployPath)
        #grunt = "sudo ssh -i '/master.pem' root@%s 'cd %s && grunt'" % (host, deployPath)
        os.system(rsync)
        os.system(chown)
        #os.system(grunt)
        #Running npm run bundle on deployPath
       	#bundle = "sudo ssh -i '/master.pem' root@%s 'cd %s && npm run bundle'" % (host, deployPath)
        #os.system(bundle)
        #print(bundle)
else:
    rsync = "sudo rsync --delete --exclude-from '%s' -avz -e 'ssh -i /master.pem' %s/ root@%s:%s" % \
                (exclude_file, workspace, destHost, deployPath)
    chown = "sudo ssh -i '/master.pem' root@%s 'chown -R nginx:nginx %s'" % (destHost, deployPath)
    #grunt = "sudo ssh -i '/master.pem' root@%s 'cd %s && grunt'" % (destHost, deployPath)
    os.system(rsync)
    os.system(chown)
    #os.system(grunt)
    #Running npm run bundle on deployPath
    #bundle = "sudo ssh -i '/master.pem' root@%s 'cd %s && npm run bundle'" % (destHost, deployPath)
    #os.system(bundle)
    #print(bundle)

    
#bundle = "sudo ssh -i '/master.pem' root@prod_hdgs_web1 'cd %s && npm run bundle'" % (deployPath)
#os.system(bundle)
#print(bundle) 

#make_tarfile(builname+"_"+buildnambuer+".tar.gz", workspace)
#shutil.move(builname+"_"+buildnambuer+".tar.gz", '/opt/builds_tar/')

#Closing log file
# sys.stdout = old_stdout
# log_file.close()
cnx.close()
exit(0)
