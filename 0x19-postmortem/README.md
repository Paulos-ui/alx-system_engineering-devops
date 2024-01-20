# Postmortem
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Overview of the issue: 
    An outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file 

## Duration:  
     The outage occurred on January 19, 2024, from 9:00am to 11:30am (PT)

## Root Cause: 
   The root cause was identified as a misconfiguration in the Apache web server's virtual host settings.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Timeline:
+ 9:00AM: The issue was detected as monitoring tools reported increased error rates and elevated response times.
+ 9:25AM: The on-call engineer received automated alerts and initiated an investigation into the issue.
+ 9:30AM:  Initial examination focused on server resource utilization and application logs. No abnormalities were found.
+ 9:35AM: Assumed the issue might be related to database connectivity issues. Spent time investigating database performance.
+ 9:50AM: Despite scaling the database temporarily, the issue persisted. Suspected potential file corruption in the WordPress installation.
+ 10:00AM:  Escalation to the DevOps team was made as further investigation revealed the Apache server misconfiguration
+ 10:30AM: Root cause identified - a misconfiguration in the Apache virtual host settings leading to incorrect file paths
+ 11:00AM: Immediate actions taken to correct the virtual host settings and restart the Apache server
+ 11:30AM:  Service fully restored after implementing the fix and verifying that GET requests returned the expected HTML file  

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Root Cause and Resolution:

+ Root Cause: The misconfiguration in the Apache virtual host settings resulted from an inadvertent change during recent updates, causing incorrect file paths for the WordPress site.

+ Resolution: The issue was resolved by correcting the virtual host settings to accurately point to the WordPress site's files. Additionally, a review process for configuration changes was implemented to prevent similar misconfigurations in the future.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Corrective and Preventative Measures:
+ Improvements/Fixes:

    Configuration Change Review Process: Establish a systematic review process for configuration changes, involving relevant teams to ensure accuracy and avoid misconfigurations.

    Automated Virtual Host Testing: Introduce automated tests in the deployment pipeline to validate the correctness of Apache virtual host configurations.

 +   Documentation Update: Revise documentation to include explicit instructions for Apache virtual host configurations and updates. 


     In summary, This postmortem not only reveals the incredible Apache adventure, but it also demonstrates our dedication to growing, learning, and bringing some fun into the software industry. We are committed to transforming every setback into an inspiring tale of success as we make our way through the wide expanses of virtual hosts and containers. Await more exciting tales from our technological saga!

 it will never occur again, because we're programmers, and we never make errors! 😉
