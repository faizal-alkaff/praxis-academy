[2019-12-01 17:19.38]  /drives/c/Users/HP/Documents
[HP.local] ➤ mkdir rhymes

[2019-12-01 17:19.45]  /drives/c/Users/HP/Documents
[HP.local] ➤ cd rhymes/

[2019-12-01 17:19.49]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git init
Initialized empty Git repository in /drives/c/Users/HP/Documents/rhymes/.git/

[2019-12-01 17:19.54]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ touch README.txt

[2019-12-01 17:20.04]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git add README.txt

[2019-12-01 17:20.10]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git commit -m 'First commit.'
[master (root-commit) a92a3d5] First commit.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.txt

[2019-12-01 17:20.26]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ echo 'This repo is a collection of my favorite nursery rhymes.' >> README.txt

[2019-12-01 17:20.33]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ cat README.txt
This repo is a collection of my favorite nursery rhymes.

[2019-12-01 17:20.49]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.txt

no changes added to commit (use "git add" and/or "git commit -a")

[2019-12-01 17:20.54]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git diff
diff --git a/README.txt b/README.txt
index e69de29..c83e022 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+This repo is a collection of my favorite nursery rhymes.

[2019-12-01 17:21.26]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git add README.txt

[2019-12-01 17:21.45]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git commit -m 'Added project overview to README.txt'
[master 1992958] Added project overview to README.txt
 1 file changed, 1 insertion(+)

[2019-12-01 17:24.22]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/text/Sample-text-file-10kb.txt
--2019-12-01 17:24:30--  https://www.sample-videos.com/text/Sample-text-file-10kb.txt
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 9510 (9.3K) [text/plain]
Saving to: `Sample-text-file-10kb.txt'

100%[===============================================================================================================================================>] 9,510       --.-K/s   in 0.05s

2019-12-01 17:24:30 (177 KB/s) - `Sample-text-file-10kb.txt' saved [9510/9510]


[2019-12-01 17:24.30]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/text/Sample-text-file-20kb.txt
--2019-12-01 17:24:47--  https://www.sample-videos.com/text/Sample-text-file-20kb.txt
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 19718 (19K) [text/plain]
Saving to: `Sample-text-file-20kb.txt'

100%[===============================================================================================================================================>] 19,718      90.4K/s   in 0.2s

2019-12-01 17:24:48 (90.4 KB/s) - `Sample-text-file-20kb.txt' saved [19718/19718]


[2019-12-01 17:24.48]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/text/Sample-text-file-50kb.txt
--2019-12-01 17:24:53--  https://www.sample-videos.com/text/Sample-text-file-50kb.txt
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 50537 (49K) [text/plain]
Saving to: `Sample-text-file-50kb.txt'

100%[===============================================================================================================================================>] 50,537       171K/s   in 0.3s

2019-12-01 17:24:54 (171 KB/s) - `Sample-text-file-50kb.txt' saved [50537/50537]


[2019-12-01 17:24.54]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/text/Sample-text-file-100kb.txt
--2019-12-01 17:24:58--  https://www.sample-videos.com/text/Sample-text-file-100kb.txt
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 102180 (100K) [text/plain]
Saving to: `Sample-text-file-100kb.txt'

100%[===============================================================================================================================================>] 102,180      274K/s   in 0.4s

2019-12-01 17:24:59 (274 KB/s) - `Sample-text-file-100kb.txt' saved [102180/102180]

[2019-12-01 17:26.36]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ ls -lrt
total 93
-rw-r--r--    1 HP       UsersGrp     50537 Nov 16  2016 Sample-text-file-50kb.txt
-rw-r--r--    1 HP       UsersGrp     19718 Nov 16  2016 Sample-text-file-20kb.txt
-rw-r--r--    1 HP       UsersGrp      9510 Nov 16  2016 Sample-text-file-10kb.txt
-rw-r--r--    1 HP       UsersGrp    102180 Nov 16  2016 Sample-text-file-100kb.txt
-rw-r--r--    1 HP       UsersGrp        57 Dec  1 17:20 README.txt

[2019-12-01 17:26.42]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git add Sample-text-file-10kb.txt

[2019-12-01 17:26.46]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   Sample-text-file-10kb.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Sample-text-file-100kb.txt
        Sample-text-file-20kb.txt
        Sample-text-file-50kb.txt

[2019-12-01 17:26.50]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git commit -m 'Added Sample-text-file-10kb.txt'
[master 0c90e8d] Added Sample-text-file-10kb.txt
 1 file changed, 27 insertions(+)
 create mode 100644 Sample-text-file-10kb.txt

[2019-12-01 17:27.50]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git add Sample-text-file-20kb.txt

[2019-12-01 17:27.59]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git commit -m 'Added Sample-text-file-20kb.txt'
[master ea6a25e] Added Sample-text-file-20kb.txt
 1 file changed, 59 insertions(+)
 create mode 100644 Sample-text-file-20kb.txt

[2019-12-01 17:28.29]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git add .

[2019-12-01 17:29.34]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git commit -m 'Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt'
[master 5ff7d98] Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt
 2 files changed, 488 insertions(+)
 create mode 100644 Sample-text-file-100kb.txt
 create mode 100644 Sample-text-file-50kb.txt

[2019-12-01 17:31.49]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git log

commit 5ff7d982812985920df481184e2762c67ba114b8 (HEAD -> master)
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:30:12 2019 +0700

    Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt

commit ea6a25ec76b7cb7998c3c44a4bde5a0d9e754951
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:28:29 2019 +0700

    Added Sample-text-file-20kb.txt

commit 0c90e8d88c8eb5ce796d3e1bc856455e801d8703
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:27:49 2019 +0700

    Added Sample-text-file-10kb.txt

commit 1992958e9c1f9dd47c8942884c02edc1b35f4b12
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:21:57 2019 +0700

    Added project overview to README.txt

commit a92a3d5edea7637f98e76e3894c94cad584124da
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:20:25 2019 +0700

    First commit.

[2019-12-01 17:32.43]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git log --oneline

commit 5ff7d982812985920df481184e2762c67ba114b8 (HEAD -> master)
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:30:12 2019 +0700

    Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt

commit ea6a25ec76b7cb7998c3c44a4bde5a0d9e754951
5ff7d98 (HEAD -> master) Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt
ea6a25e Added Sample-text-file-20kb.txt
0c90e8d Added Sample-text-file-10kb.txt
1992958 Added project overview to README.txt
a92a3d5 First commit.

[2019-12-01 17:35.11]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git log -p

commit 5ff7d982812985920df481184e2762c67ba114b8 (HEAD -> master)
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:30:12 2019 +0700

    Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt

commit ea6a25ec76b7cb7998c3c44a4bde5a0d9e754951
5ff7d98 (HEAD -> master) Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt
ea6a25e Added Sample-text-file-20kb.txt
0c90e8d Added Sample-text-file-10kb.txt
1992958 Added project overview to README.txt
a92a3d5 First commit.

~
~
~
~
commit 5ff7d982812985920df481184e2762c67ba114b8 (HEAD -> master)
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 17:30:12 2019 +0700

    Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt

diff --git a/Sample-text-file-100kb.txt b/Sample-text-file-100kb.txt
new file mode 100644
index 0000000..0d39db3
--- /dev/null
+++ b/Sample-text-file-100kb.txt
@@ -0,0 +1,327 @@
+Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus condimentum sagittis lacus, laoreet luctus ligula laoreet ut. Vestibulum ullamcorper accumsan velit vel v
ehicula. Proin tempor lacus arcu. Nunc at elit condimentum, semper nisi et, condimentum mi. In venenatis blandit nibh at sollicitudin. Vestibulum dapibus mauris at orci maximus pellent
esque. Nullam id elementum ipsum. Suspendisse cursus lobortis viverra. Proin et erat at mauris tincidunt porttitor vitae ac dui.M
+M
............

# Create new repo named "rhymes"

[2019-12-01 17:35.12]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote add origin https://github.com/faizal-alkaff/rhymes.git

[2019-12-01 17:40.53]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git push -u origin master
Username for 'https://github.com':
Password for 'https://faizal-alkaff@github.com':
Counting objects: 16, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (13/13), done.
Writing objects: 100% (16/16), 41.27 KiB | 1.12 MiB/s, done.
Total 16 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), done.
To https://github.com/faizal-alkaff/rhymes.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

[2019-12-01 17:45.28]  /drives/c/Users/HP/Documents
[HP.local] ➤ mkdir other-user

[2019-12-01 17:45.42]  /drives/c/Users/HP/Documents
[HP.local] ➤ cd other-user/

[2019-12-01 17:46.35]  /drives/c/Users/HP/Documents/other-user
[HP.local] ➤ git clone https://github.com/faizal-alkaff/rhymes.git
Cloning into 'rhymes'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 16 (delta 4), reused 16 (delta 4), pack-reused 0
Unpacking objects: 100% (16/16), done.

[2019-12-01 17:46.48]  /drives/c/Users/HP/Documents/other-user
[HP.local] ➤ ls -lrt
total 2
drwxr-xr-x    1 HP       UsersGrp         0 Dec  1 17:46 rhymes

[2019-12-01 17:48.04]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git checkout -b hickory-dickory
Switched to a new branch 'hickory-dickory'

[2019-12-01 17:48.31]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv
--2019-12-01 17:49:36--  https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 1098 (1.1K) [text/csv]
Saving to: `Sample-Spreadsheet-10-rows.csv'

100%[===============================================================================================================================================>] 1,098       --.-K/s   in 0s

2019-12-01 17:49:36 (44.4 MB/s) - `Sample-Spreadsheet-10-rows.csv' saved [1098/1098]

[2019-12-01 17:50.06]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git add Sample-Spreadsheet-10-rows.csv

[2019-12-01 17:50.10]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -m 'Added Sample-Spreadsheet-10-rows.csv'
[hickory-dickory 0bd2f99] Added Sample-Spreadsheet-10-rows.csv
 1 file changed, 10 insertions(+)
 create mode 100644 Sample-Spreadsheet-10-rows.csv

[2019-12-01 17:50.28]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git push origin hickory-dickory
Username for 'https://github.com':
Password for 'https://faizal-alkaff@github.com':
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 947 bytes | 135.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'hickory-dickory' on GitHub by visiting:
remote:      https://github.com/faizal-alkaff/rhymes/pull/new/hickory-dickory
remote:
To https://github.com/faizal-alkaff/rhymes.git
 * [new branch]      hickory-dickory -> hickory-dickory



[2019-12-01 17:51.58]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ cd ../../rhymes/

[2019-12-01 18:02.47]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote rename origin faizal

[2019-12-01 18:09.55]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote
faizal

[2019-12-01 18:10.52]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote -v
faizal  https://github.com/faizal-alkaff/rhymes.git (fetch)
faizal  https://github.com/faizal-alkaff/rhymes.git (push)

[2019-12-01 18:03.00]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote add alkaff https://github.com/faizal-alkaff/rhymes.git

[2019-12-01 18:04.04]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote
alkaff
faizal

[2019-12-01 18:04.12]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git remote -v
alkaff  https://github.com/faizal-alkaff/rhymes.git (fetch)
alkaff  https://github.com/faizal-alkaff/rhymes.git (push)
faizal  https://github.com/faizal-alkaff/rhymes.git (fetch)
faizal  https://github.com/faizal-alkaff/rhymes.git (push)

[2019-12-01 18:19.26]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git fetch alkaff

[2019-12-01 18:19.25]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git branch -a
* master
  remotes/alkaff/hickory-dickory
  remotes/alkaff/master
  remotes/faizal/master

[2019-12-01 18:21.18]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git checkout -b hickory-dickory alkaff/hickory-dickory
Branch 'hickory-dickory' set up to track remote branch 'hickory-dickory' from 'alkaff'.
Switched to a new branch 'hickory-dickory'

[2019-12-01 18:23.33]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git diff master hickory-dickory

diff --git a/Sample-Spreadsheet-10-rows.csv b/Sample-Spreadsheet-10-rows.csv
new file mode 100644
index 0000000..b345028
--- /dev/null
+++ b/Sample-Spreadsheet-10-rows.csv
@@ -0,0 +1,10 @@
+1,"Eldon Base for stackable storage shelf, platinum",Muhammed MacIntyre,3,-213.25,38.94,35,Nunavut,Storage & Organization,0.8M
+2,"1.7 Cubic Foot Compact ""Cube"" Office Refrigerators",Barry French,293,457.81,208.16,68.02,Nunavut,Appliances,0.58M
+3,"Cardinal Slant-D▒ Ring Binder, Heavy Gauge Vinyl",Barry French,293,46.71,8.69,2.99,Nunavut,Binders and Binder Accessories,0.39M
+4,R380,Clay Rozendal,483,1198.97,195.99,3.99,Nunavut,Telephones and Communication,0.58M
+5,Holmes HEPA Air Purifier,Carlos Soltero,515,30.94,21.78,5.94,Nunavut,Appliances,0.5M
+6,G.E. Longer-Life Indoor Recessed Floodlight Bulbs,Carlos Soltero,515,4.43,6.64,4.95,Nunavut,Office Furnishings,0.37M
+7,"Angle-D Binders with Locking Rings, Label Holders",Carl Jackson,613,-54.04,7.3,7.72,Nunavut,Binders and Binder Accessories,0.38M
+8,"SAFCO Mobile Desk Side File, Wire Frame",Carl Jackson,613,127.70,42.76,6.22,Nunavut,Storage & Organization,M
+9,"SAFCO Commercial Wire Shelving, Black",Monica Federle,643,-695.26,138.14,35,Nunavut,Storage & Organization,M
+10,Xerox 198,Dorothy Badders,678,-226.36,4.98,8.33,Nunavut,Paper,0.38M

[2019-12-01 18:27.28]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git checkout master
Switched to branch 'master'
Your branch is up to date with 'faizal/master'.

[2019-12-01 18:27.48]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git merge hickory-dickory
Updating 5ff7d98..0bd2f99
Fast-forward
 Sample-Spreadsheet-10-rows.csv | 10 ++++++++++
 1 file changed, 10 insertions(+)
 create mode 100644 Sample-Spreadsheet-10-rows.csv

[2019-12-01 18:28.14]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ ls -lrt
total 95
-rw-r--r--    1 HP       UsersGrp     50537 Nov 16  2016 Sample-text-file-50kb.txt
-rw-r--r--    1 HP       UsersGrp     19718 Nov 16  2016 Sample-text-file-20kb.txt
-rw-r--r--    1 HP       UsersGrp      9510 Nov 16  2016 Sample-text-file-10kb.txt
-rw-r--r--    1 HP       UsersGrp    102180 Nov 16  2016 Sample-text-file-100kb.txt
-rw-r--r--    1 HP       UsersGrp        57 Dec  1 17:20 README.txt
-rw-r--r--    1 HP       UsersGrp      1098 Dec  1 18:28 Sample-Spreadsheet-10-rows.csv

[2019-12-01 18:31.56]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ git branch -D hickory-dickory
Deleted branch hickory-dickory (was 0bd2f99).

[2019-12-01 18:43.01]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ cd ../other-user/rhymes/

[2019-12-01 18:43.07]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote rm alkaff

[2019-12-01 18:43.34]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote -v
origin  https://github.com/faizal-alkaff/rhymes.git (fetch)
origin  https://github.com/faizal-alkaff/rhymes.git (push)

[2019-12-01 18:43.42]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ cd -
/drives/c/Users/HP/Documents/rhymes

[2019-12-01 18:43.46]  /drives/c/Users/HP/Documents/rhymes
[HP.local] ➤ cd ../other-user/rhymes/

[2019-12-01 18:43.55]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote rename origin alkaff

[2019-12-01 18:44.01]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote add faizal https://github.com/faizal-alkaff/rhymes.git

[2019-12-01 18:44.33]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote -v
alkaff  https://github.com/faizal-alkaff/rhymes.git (fetch)
alkaff  https://github.com/faizal-alkaff/rhymes.git (push)
faizal  https://github.com/faizal-alkaff/rhymes.git (fetch)
faizal  https://github.com/faizal-alkaff/rhymes.git (push)

[2019-12-01 18:44.41]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote
alkaff
faizal

[2019-12-01 18:44.51]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git remote update
Fetching alkaff
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), done.
From https://github.com/faizal-alkaff/rhymes
   5ff7d98..788c109  master     -> alkaff/master
Fetching faizal
From https://github.com/faizal-alkaff/rhymes
 * [new branch]      hickory-dickory -> faizal/hickory-dickory
 * [new branch]      master          -> faizal/master

[2019-12-01 18:45.30]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git checkout master
Switched to branch 'master'
Your branch is behind 'alkaff/master' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

[2019-12-01 18:45.50]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git merge faizal/master
Updating 5ff7d98..788c109
Fast-forward
 Sample-Spreadsheet-10-rows.csv | 10 ++++++++++
 1 file changed, 10 insertions(+)
 create mode 100644 Sample-Spreadsheet-10-rows.csv

[2019-12-01 18:46.02]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ ls -lrt
total 95
-rw-r--r--    1 HP       UsersGrp     50537 Dec  1 17:46 Sample-text-file-50kb.txt
-rw-r--r--    1 HP       UsersGrp     19718 Dec  1 17:46 Sample-text-file-20kb.txt
-rw-r--r--    1 HP       UsersGrp      9510 Dec  1 17:46 Sample-text-file-10kb.txt
-rw-r--r--    1 HP       UsersGrp    102180 Dec  1 17:46 Sample-text-file-100kb.txt
-rw-r--r--    1 HP       UsersGrp        57 Dec  1 17:46 README.txt
-rw-r--r--    1 HP       UsersGrp      1098 Dec  1 18:46 Sample-Spreadsheet-10-rows.csv

[2019-12-01 18:46.48]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git diff faizal/master

[2019-12-01 18:47.27]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git push alkaff master
Username for 'https://github.com':
Password for 'https://faizal-alkaff@github.com':
Everything up-to-date

[2019-12-01 18:47.54]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git checkout -b alkaff-changes
Switched to a new branch 'alkaff-changes'

[2019-12-01 18:48.24]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg
--2019-12-01 18:50:17--  https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 51085 (50K) [image/jpeg]
Saving to: `Sample-jpg-image-50kb.jpg'

100%[===============================================================================================================================================>] 51,085       151K/s   in 0.3s

2019-12-01 18:50:18 (151 KB/s) - `Sample-jpg-image-50kb.jpg' saved [51085/51085]


[2019-12-01 18:50.18]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git add Sample-jpg-image-50kb.jpg

[2019-12-01 18:50.45]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -m 'Added Sample-jpg-image-50kb.jpg'
[alkaff-changes 28de0d5] Added Sample-jpg-image-50kb.jpg
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Sample-jpg-image-50kb.jpg

[2019-12-01 18:51.00]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/img/Sample-jpg-image-100kb.jpg
--2019-12-01 18:51:24--  https://www.sample-videos.com/img/Sample-jpg-image-100kb.jpg
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 102796 (100K) [image/jpeg]
Saving to: `Sample-jpg-image-100kb.jpg'

100%[===============================================================================================================================================>] 102,796      192K/s   in 0.5s

2019-12-01 18:51:25 (192 KB/s) - `Sample-jpg-image-100kb.jpg' saved [102796/102796]


[2019-12-01 18:51.25]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git add Sample-jpg-image-100kb.jpg

[2019-12-01 18:51.37]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -m 'Added Sample-jpg-image-100kb.jpg'
[alkaff-changes 5660b34] Added Sample-jpg-image-100kb.jpg
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Sample-jpg-image-100kb.jpg

[2019-12-01 19:36.17]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ vi README.txt

[2019-12-01 19:36.25]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ cat README.txt
This repo is a collection of faizal favorite nursery rhymes.

[2019-12-01 19:36.30]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -am 'Updated README.txt.'
[alkaff-changes 8762611] Updated README.txt.
 1 file changed, 1 insertion(+), 1 deletion(-)

[2019-12-01 19:40.26]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ vi README.txt

diff --git a/README.txt b/README.txt
index 005c03b..2b7a790 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1 @@
This repo is a collection of [-faizal-]{+Faizal+} favorite nursery rhymes. {+Pull requests accepted.+}

[2019-12-01 19:40.29]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -am 'Fixed typo in README.txt.'
[alkaff-changes 3b1b82f] Fixed typo in README.txt.
 1 file changed, 1 insertion(+), 1 deletion(-)

[2019-12-01 19:40.40]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ wget --no-check-certificate https://www.sample-videos.com/ppt/Sample-PPT-File-500kb.ppt
--2019-12-01 19:44:03--  https://www.sample-videos.com/ppt/Sample-PPT-File-500kb.ppt
Resolving www.sample-videos.com... 3.6.20.22
Connecting to www.sample-videos.com|3.6.20.22|:443... connected.
WARNING: no certificate subject alternative name matches
        requested host name `www.sample-videos.com'.
HTTP request sent, awaiting response... 200 OK
Length: 527872 (516K) [application/vnd.ms-powerpoint]
Saving to: `Sample-PPT-File-500kb.ppt'

100%[===============================================================================================================================================>] 527,872      328K/s   in 1.6s

2019-12-01 19:44:06 (328 KB/s) - `Sample-PPT-File-500kb.ppt' saved [527872/527872]

[2019-12-01 19:44.37]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git add Sample-PPT-File-500kb.ppt

[2019-12-01 19:44.50]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -m 'Added Sample-PPT-File-500kb.ppt'
[alkaff-changes df4c849] Added Sample-PPT-File-500kb.ppt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Sample-PPT-File-500kb.ppt

[2019-12-01 19:52.32]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ vi README.txt

[2019-12-01 19:53.00]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -am 'Updated README.txt.'
[alkaff-changes 126e047] Updated README.txt.
 1 file changed, 1 insertion(+), 1 deletion(-)

[2019-12-01 19:53.05]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ vi README.txt

[2019-12-01 19:53.19]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -am 'Updated README.txt.'
[alkaff-changes 9d32a77] Updated README.txt.
 1 file changed, 1 insertion(+), 1 deletion(-)

[2019-12-01 19:53.23]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ vi README.txt

[2019-12-01 19:53.43]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git commit -am 'Updated README.txt.'
[alkaff-changes 7e8536f] Updated README.txt.
 1 file changed, 1 insertion(+), 1 deletion(-)

commit 7e8536f78147cf896bc7bd4c9fb6fcc6a37c5c41 (HEAD -> alkaff-changes)
Author: U-LOCAL\HP <alkaff.faizal@gmail.com>
Date:   Sun Dec 1 19:53:47 2019 +0700

7e8536f (HEAD -> alkaff-changes) Updated README.txt.
9d32a77 Updated README.txt.
126e047 Updated README.txt.
df4c849 Added Sample-PPT-File-500kb.ppt
3b1b82f Fixed typo in README.txt.
8762611 Updated README.txt.
5660b34 Added Sample-jpg-image-100kb.jpg
28de0d5 Added Sample-jpg-image-50kb.jpg
788c109 (faizal/master, alkaff/master, alkaff/HEAD, master) Merge pull request #1 from faizal-al
kaff/hickory-dickory
0bd2f99 (faizal/hickory-dickory, alkaff/hickory-dickory, hickory-dickory) Added Sample-Spreadsheet-10-rows.csv
5ff7d98 Added Sample-text-file-50kb.txt, Sample-text-file-100kb.txt
ea6a25e Added Sample-text-file-20kb.txt
0c90e8d Added Sample-text-file-10kb.txt
1992958 Added project overview to README.txt
a92a3d5 First commit.

[2019-12-01 20:18.37]  /drives/c/Users/HP/Documents/other-user/rhymes
[HP.local] ➤ git push -u alkaff alkaff-changes
Username for 'https://github.com':
Password for 'https://faizal-alkaff@github.com':
Counting objects: 24, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (24/24), done.
Writing objects: 100% (24/24), 551.75 KiB | 7.36 MiB/s, done.
Total 24 (delta 8), reused 0 (delta 0)
remote: Resolving deltas: 100% (8/8), completed with 1 local object.
remote:
remote: Create a pull request for 'alkaff-changes' on GitHub by visiting:
remote:      https://github.com/faizal-alkaff/rhymes/pull/new/alkaff-changes
remote:
To https://github.com/faizal-alkaff/rhymes.git
 * [new branch]      alkaff-changes -> alkaff-changes
Branch 'alkaff-changes' set up to track remote branch 'alkaff-changes' from 'alkaff'.