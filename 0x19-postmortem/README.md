# Postmortem

__Issue Summary:__  
From 15 Feb at 00:25AM 2022 to 16 Feb at 3:36PM (UTC-05), Apache is returning 500 error impacting 100% of server traffic leave them without can access to the service.
The root cause was a type error in a apache file configuration.

__Timeline__
All times are in UTC-05

- 00:00 AM - Configuration push begins
- 00:25 AM - Outage begins
- 09:15 AM - Problem is detected by our engineers noticed a 500 response error.
- 10:18 AM - Debugging apache configuration files.
- 02:48 PM - Founded type error in a file apache configuration.
- 03:10 PM - Make a puppet file for fix type problem in apache configuration file.
- 03:30 PM - Server restart begins
- 03:36 PM - 100% of traffic back online.

__Root cause and resolution__  
Root cause was a type error in the wordpress configuration files scripts that configurated php in apache server can to be fixed with a puppet file script that change this type and path of this file.

__Corrective and preventative measures__  
In the last days we've conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issues and to help prevent recurrence and improve response times:

- Make a review code more extented
- Change times for make push in office hours
- Improve process for detect error or bugs

</br>
</br>
</br>
Sincerely,
</br>
</br>
José Valdiviezo

Software Reability Engineer.
