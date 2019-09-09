#! /usr/bin/python

# Description. : Tool to find out Github organization Top Repos by number of Stars/Forks/Pulls/Contribution
# Created On.  : Sep 08, 2019
# Ticket No.   : Jira-XXXX
# Created by.  : Anand Subramanian
# Organization : XXXXXX
# Usage        : This tool will  analyzes the popularity of an organization's GitHub repos based on 
#                   * Top-N repos by number of stars
#                   * Top-N repos by number of forks
#                   * Top-N repos by number of Pull Requests (PRs)
#                   * Top-N repos by contribution percentage (PRs/forks)
# Input        : You need to provide the input as command-line arguments. Please refer --help for more info.
# Platform Req.: python 2.6 and above

# Standard module
import argparse
import os

# Positive integer check and use it in argparse
def positiveinteger(value):
   ivalue = int(value)
   if ivalue <= 0:
      raise argparse.ArgumentTypeError("invalid positiveinteger value:" %value)
   return ivalue

# Users input
parser = argparse.ArgumentParser(description='Find out Github Top Repos by number of Stars/Forks/Pulls/Contribution')
parser.add_argument("-orgname", "--organization", metavar='', help="Please input Organization name", required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-ts", "--topstar", type=positiveinteger, metavar='', help="Please input top Star value as Positive Integer")
group.add_argument("-tf", "--topfork", type=positiveinteger, metavar='', help="Please input top Fork value as Positive Integer")
group.add_argument("-tp", "--toppull", type=positiveinteger, metavar='', help="Please input top Pull value as Positive Integer")
group.add_argument("-tc", "--topcontribution", type=positiveinteger, metavar='', help="Please input top Contribution value as Positive Integer")
args = parser.parse_args()

organizationname=str(args.organization)
star=str(args.topstar)
fork=str(args.topfork)
pull=str(args.toppull)
contribution=str(args.topcontribution)

# JSON filter
jqfilter = "'.items[]? .name'"

# Top star (ts) repos in the organization
if args.topstar:
   print("...................Output of Top " + star + " Stars Repos....................")
   resulttopstar = os.popen('curl --silent https://api.github.com/search/repositories?q=org:' + organizationname + '+stars:' + star + ' | jq -r ' + jqfilter).read()
   if (len(resulttopstar) == 0):
      print("No matching output for top " + star + " stars in given organization repo")
   else:
      print(resulttopstar.rstrip("\n"))

# Top forks (tf) repos in the organization
if args.topfork:
   print("...................Output of Top " + fork + " Forks Repos....................")
   resulttopfork = os.popen('curl --silent https://api.github.com/search/repositories?q=org:' + organizationname + '+forks:' + fork + ' | jq -r ' + jqfilter).read()
   if (len(resulttopfork) == 0):
      print("No matching output for top " + fork + " forks in given organization repo")
   else:
      print(resulttopfork.rstrip("\n"))

# Top pull (tp) repos in the organization
if args.toppull:
   print("...................Output of Top " + pull + " Pulls Repos....................")
   resulttoppull = os.popen('curl --silent https://api.github.com/search/repositories?q=org:' + organizationname + '+pulls:' + pull + ' | jq -r ' + jqfilter).read()
   if (len(resulttoppull) == 0):
      print("No matching output for top " + pull + " pulls in given organization repo")
   else:
      print(resulttoppull.rstrip("\n"))

# Top  contribution (tc) repos in the organization
if args.topcontribution:
   print("...................Output of Top " + contribution + " Forks&Pulls Repos....................")
   resulttopcontribution = os.popen('curl --silent https://api.github.com/search/repositories?q=org:' + organizationname + '+forks:' + contribution + '+pulls:' + contribution + ' | jq -r ' + jqfilter).read()
   if (len(resulttopcontribution) == 0):
      print("No matching output for top " + contribution + " Forks&Pulls in given organization repo")
   else:
      print(resulttopcontribution.rstrip("\n"))

# End of the program
