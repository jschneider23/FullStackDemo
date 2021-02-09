# TD Ameritrade Full-Stack Web App Demo: <br>*A Flask Web App with a Bootstrap Frontend Built on TD Ameritrade's Stock Market Developer APIs*
### Developed by Jason Schneider (as a COVID-19 Pandemic side project)<br>Web App Link Here: [App Deployed on Heroku](http://localhost:5000/)


## Quick Links
* **App Features, Use, and Demonstration Video:** [Link](https://videolinkplaceholder.com)
* **My LinkedIn:** [Link](https://www.linkedin.com/in/jason-schneider-772a19173/)
* TD Ameritrade Developer APIs and Documentation: [Link](https://developer.tdameritrade.com/apis)
* TD Ameritrade Symbol Lookup (Used in Implementation): [Link](https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp)
* Flask Web Framework: [Link](https://flask.palletsprojects.com/en/1.1.x/)
* Bootstrap 4 Documentation: [Link](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Table of Contents
* FAQs
* TD Ameritrade APIs

## "FAQs" For Interested Employers, Recruiters, and Organizations

### What was the purpose of this web app project?

The purpose of this project was to be a **personal side project** that refreshed, sharpened, and further developed my skills in **full-stack development** (as well as the languages and tools used in the project individually) during a pandemic that interrupted my original post-graduation plans.  Given that we had, and still have, no idea how much longer this pandemic might last, I wanted to work on a practical side project for an **hour or two every day on average** so that I could use my time during the pandemic productively and **gain more experience, knowledge, and insight** as a full-stack developer.

This project was also a great opportunity to learn more about a personal interest of mine: **the stock market.**  I eventually plan to develop a predictive model for personal investments down the line, and this project was able to give me experience with APIs I likely want to use as well as **methods of handling, processing, and understanding raw stock market data**.  My involvement with this project will serve as invaluable resource and reference when I do decide to develop that for myself, after further research and experience of course.

### What are the main features of this app?
List main features here

### What languages, technologies, and skills were used?
**Data API**: TD Ameritrade's Developer APIs *(app licensed under my personal account)*<br>
**Backend**: *Python 3.7.3* with the main libraries being *Pandas, Requests, Plotly, and Datetime*<br>
**Framework**: *Flask Web Framework*<br>
**Frontend/UI**: Plain *JavaScript*, *jQuery*, and *HTML/CSS (using Bootstrap 4)*

### What challenges did I face and how did I overcome them or deal with them?

The largest problem I faced wasn't an issue with code, development, or a bug: it was the **COVID-19 Pandemic**.  The pandemic has hit everyone hard and differently, whether we or a loved one has actually contracted it or not.  While I have been fortunate so far as to not contract it myself, the pandemic has certainly **impacted my mental health and capacity noticeably**.  While the manner in which it has affected these things is a private matter, it certainly had the largest impact on this project out of any of the challenges I faced.  Despite the difficulty the situation posed for me, I saw this project idea as an **opportunity to not only recover from the impacts of the pandemic, but also to grow as a developer** due to the less-than-desired conditions that can frequently come up during development on a larger scale.  I was able to push through this adveristy with **dedication and persistance** to **achieve the purposes and goals I set** for this project and present it to anyone who may be interested.

The next largest issue I faced was **undocumented and unexpected functionality when requesting TD Ameritrade's Option Chains API** that I needed to handle on my end to **fulfill expected and desired implementation and functionality**.  You can read more about this specific API [here](https://developer.tdameritrade.com/option-chains/apis/get/marketdata/chains), but to summarize the API and where the actual functionality differs than what is expected:
> The Options Chain API takes a variety of parameters in its query string: some optional, some with defaults, and only one parameter that is required for proper functionality, which is the **symbol** (need to know which symbol to get an option chain for).  Many of these parameters are designed and intended to work at the same time to filter results to certain criteria, however, **some cannot be combined or else the API will return useless results, no results or an error**.
> 
> An example of two parameters that **can and should be combined** (aside from symbol and any other parameter) are **contractType** *(calls, puts, or calls & puts)* and **expMonth** *(only show an options expiring in this month)*.  This functions **as expected**: if I wanted **only calls expiring in March** for a certain symbol, the request would return a JSON with **options contracts that are calls expiring in March** *(which could be no results, if there aren't any contracts for this symbol expiring in March)*
> 
> An example of some parameters that **can't and should not be combined** are **fromDate and toDate** *(only get options contracts expiring between these dates)* and then a completely different **expMonth**.  Since these **both specify a time period of valid options contracts**, the time periods will almost always **conflict** and therefore **should not be combined**.  While they technically can be combined from the API's perspective, this doesn't make any sense when using the API as a data source, so the **app UI disables the Expiration Month field if a date is entered into the Expriations From/To Date and vice versa**.
> 
> 

### What did I learn and/or gain from this experience?
Answer placeholder

## TD Ameritrade Developer APIs
Explanation Here
## Backend Modules and Functions
Documentation Here
## Framework and Hosting
More Documentation Here
## Frontend and UI/UX
More Documentation Here