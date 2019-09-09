Description. : Tool to find out Github organization Top Repos by number of Stars/Forks/Pulls/Contribution
Created On.  : Sep 08, 2019
Ticket No.   : Jira-XXXX
Created by.  : Anand Subramanian
Organization : XXXXXX
Usage        : This tool will  analyzes the popularity of an organization GitHub repos based on 
                   * Top-N repos by number of stars
                   * Top-N repos by number of forks
                   * Top-N repos by number of Pull Requests (PRs)
                   * Top-N repos by contribution percentage (PRs/forks)
Input         : You need to provide the input as command-line arguments. Please refer --help for more info
Requirement. : python 2.6 and above

How to Run this Tool:

1. First run this script using --help to find out options. For example,

python GitRepoSearch.py --help
usage: GitRepoSearch.py [-h] -orgname  [-ts] [-tf] [-tp] [-tc]

Find out Github Top Repos by number of Stars/Forks/Pulls/Contribution

optional arguments:
  -h, --help            show this help message and exit
  -orgname , --organization 
                        Please input Organization name
  -ts , --topstar       Please input top Star value as Positive Integer
  -tf , --topfork       Please input top Fork value as Positive Integer
  -tp , --toppull       Please input top Pull value as Positive Integer
  -tc , --topcontribution 
                        Please input top Contribution value as Positive
                        Integer

2. Now, you can provide your input(s).  For example,

python GitRepoSearch.py -orgname github -ts 10
...................Output of Top 10 Stars Repos....................
gitcasts
debug-repo
cas-overlay


python GitRepoSearch.py -orgname github -tf 10
...................Output of Top 10 Forks Repos....................
tab-container-element
custom-element-boilerplate
task-lists-element
auto-check-element
windows-msysgit

python GitRepoSearch.py -orgname github -ts 50 -tf 8
...................Output of Top 50 Stars Repos....................
tainted_hash
libprojfs
...................Output of Top 8 Forks Repos....................
babel-plugin-transform-custom-element-classes
chatops-controller
gem-builder
safegem
nagios-plugins-github

3. And this tools must require 'orgname' paramter, other paramters in Positive Integer. For example,

python GitRepoSearch.py
usage: god.py [-h] -orgname  [-ts] [-tf] [-tp] [-tc]
god.py: error: argument -orgname/--organization is required

python GitRepoSearch.py -orgname github -ts ten
usage: god.py [-h] -orgname  [-ts] [-tf] [-tp] [-tc]
god.py: error: argument -ts/--topstar: invalid positiveinteger value: 'ten'

python GitRepoSearch.py -orgname github -ts -14
usage: god.py [-h] -orgname  [-ts] [-tf] [-tp] [-tc]
god.py: error: argument -ts/--topstar: invalid positiveinteger value: '-14'
