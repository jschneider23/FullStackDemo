# TD Ameritrade Full-Stack Web App Demo: <br>*A Flask Web App with a Bootstrap Frontend Built on TD Ameritrade's Stock Market Developer APIs*
<center>
	<h3>Web App Link Here: [Deployed on Heroku](http://localhost:5000/)<br>
	Developed by Jason Schneider<br>
	(*Contact Me: jasondukeschneider@gmail.com*)
</center>

##### <u>IMPORTANT NOTICES</u>:<br>-> Heroku's free tier for web hosting will automatically put to sleep any free site/app after 30 minutes of inactivity, so the app may take around 10 seconds to initially wake and load if you are the first to navigate to the link in a while.<br>-> The API Key visible in the bd_config.py file is intentionally visible for code review purposes (so you can get an idea as to what one may look like) *as it was only active during development and has since been deactivated and replaced by a new API Key on the Heroku repository.*


## Quick Links
* **App Features, Use, and Demonstration Video:** [Link](https://videolinkplaceholder.com)
* **My LinkedIn:** [Link](https://www.linkedin.com/in/jason-schneider-772a19173/)
* TD Ameritrade *(sometimes referenced as TDA in other sections)* Developer APIs and Documentation: [Link](https://developer.tdameritrade.com/apis)
* TD Ameritrade Symbol Lookup (Used in Implementation): [Link](https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp)
* Flask Web Framework: [Link](https://flask.palletsprojects.com/en/1.1.x/)
* Bootstrap 4 Documentation: [Link](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Table of Contents
* ["FAQs" For Interested Employers, Recruiters, and Organizations](#faqs-for-interested-employers-recruiters-and-organizations)
* TD Ameritrade APIs

## "FAQs" For Interested Employers, Recruiters, and Organizations

### What languages and technologies were used?
**Data API**: TD Ameritrade's Developer APIs *(app licensed under my personal account)*<br>
**Backend**: *Python 3.7.3* with the main libraries being *Pandas, Requests, Plotly, and Datetime*<br>
**Framework**: *Flask Web Framework*<br>
**Frontend/UI**: Plain *JavaScript*, *jQuery*, and *HTML/CSS (using Bootstrap 4)*

### What was the purpose of this web app project?

The purpose of this project was to be a **personal side project** that refreshed, sharpened, and further developed my skills in **full-stack development** (as well as the languages and tools used in the project individually) during a pandemic that interrupted my original post-graduation plans.  Given that we had, and still have, no idea how much longer this pandemic might last, I wanted to work on a practical side project for an **hour or two every day on average** so that I could use my time during the pandemic productively and **gain more experience, knowledge, and insight** as a full-stack developer.

This project was also a great opportunity to learn more about a personal interest of mine: **the stock market.**  I eventually plan to develop a predictive model for personal investments down the line, and this project was able to give me experience with APIs I likely want to use as well as **methods of handling, processing, and understanding raw stock market data**.  My involvement with this project will serve as invaluable resource and reference when I do decide to develop that for myself, after further research and experience of course.

### What are the main features the web app demo?
List main features here

### What challenges did I face and how did I overcome them or deal with them?

#### COVID-19 Pandemic
The largest problem I faced wasn't an issue with code, development, or a bug: it was the **COVID-19 Pandemic**.  The pandemic has hit everyone hard and differently, whether we or a loved one has actually contracted it or not.  While I have been fortunate so far as to not contract it myself, the pandemic has certainly **impacted my mental health and capacity noticeably**, and also has had me worried about family members and relatives who are at risk.  While the manner in which it has affected these things is a private matter, it certainly had the largest impact on this project out of any of the challenges I faced.  Despite the difficulty the situation posed for me, I saw this project idea as an **opportunity to not only recover from the impacts of the pandemic, but also to grow as a developer** due to the less-than-desired conditions that can frequently come up during development on a larger scale.  I was able to push through this adveristy with **dedication and persistance** to **achieve the purposes and goals I set** for this project and present it to anyone who may be interested.

#### Unexpected TDA Options Chain API Parameter/Filter Interaction
The next largest issue I faced was **undocumented and unexpected functionality when requesting TD Ameritrade's Option Chains API** that I needed to handle on my end to **fulfill expected and desired implementation and functionality**.  You can read more about this specific API [here](https://developer.tdameritrade.com/option-chains/apis/get/marketdata/chains).

##### Brief Summary of the API, Examples of Proper Functionality, and the Unexpected Functionality

The Options Chain API takes a variety of parameters in its query string: some optional, some with defaults, and only one parameter that is required for proper functionality, which is the **symbol** (need to know which symbol to get an option chain for).  Many of these parameters are designed and intended to work at the same time to filter results to certain criteria, however, **some cannot be combined or else the API will respond with useless results, no results or an error**.

An example of two parameters that **can and should be combined** (aside from symbol and any other parameter) are **contractType** *(calls, puts, or calls & puts)* and **expMonth** *(only show an options expiring in this month)*.  This functions **as expected**: if I wanted **only calls expiring in March** for a certain symbol, the request would respond with a JSON with **options contracts that are calls expiring in March** *(which could be no results, if there aren't any contracts for this symbol expiring in March)*

An example of some parameters that **can't and should not be combined** are **fromDate and toDate** *(only get options contracts expiring between these dates)* and then a completely different **expMonth**.  Since these **both specify a time period of valid options contracts**, the time periods will almost always **conflict** and therefore **should not be combined**.  While they technically can be combined from the API's perspective, this doesn't make any sense when using the API as a data source, so the **app UI disables the Expiration Month field if a date is entered into the Expriations From/To Date and vice versa**.

The functionality issue arose when combining **numContracts** *(renamed to <b>numStrikes</b> in code and UI as this parameter actually specifies the number of strike prices returned, with each strike price having one or two associated contracts depending on contractType setting)* and **range** *(in/out/near-the-money, strikes-at/below/near-market, or all possible contracts)*.  If a **range value other than ALL, SAK, SBK, or SNK** is sent to the API, the value of **numContracts is completely ignored** and the **response will be the exact same regardless of what numContracts value it is given**.  This is not the functionality that is expected and takes away a control feature I want the user to have.  Since I can't edit the API source code, I came up with a different solution.

##### Solution: the trulyApplyFilters function

Aside from disabling incompatible parameter combinations via javaScript, I created a function that *manually applies* **numContracts <i>(aka numStrikes)</i>** after allowing the API to apply the **range** first that takes the following parameters:

```python
def trulyApplyFilters(info, numStrikes, rng):
```

The first parameter, **info**, is a dictionary containing the underlying price of a certain symbol, and then either a dataframe for calls or a dataframe for puts, or a dataframe for both.  **numStrikes** and **rng** *(stands for range, since range is a keyword in python already)* are passed from the parent function it is used in, but are the exact same values inputted by the user in the UI.  The code in this function will only run if the range value is **ITM, OTM, or NTM** and **numStrikes is not an empty string**.  If these conditions are met, it will loop through the dataframe(s) in info manually and **drop any rows** representing contracts within the same expiration date group that **exceed the max numStrikes provided**.  It then re-indexes the dataframes to ensure that they will still display properly in the Option Chain Modal.  You can learn more about how this is done specifically by looking at the source code in the repository.

#### Webscraping TD Ameritrade's Symbol Look Results for App's "Search By Name" Feature

Stuff here

#### Candlestick Chart Rendering and Timeframe Option Button onClick Events

Displaying **price history candlestick charts** for a symbol to the user as well as allowing them to **select a timeframe option** *(for example, displaying a price history chart for TSLA over the past 3 months)*, something most stock market websites and applications provide, was a key feature that needed to be included and created some troublesome issues.

##### Chart Processing, Creation, and Rendering

**Originally** I planned on sending a dictionary/json to the flask server containing all necessary format settings, information, and price history data, and then using **canvas.js** to create and render this chart on the frontend when necessary.  I had planned on handling this feature in this way throughout a decent portion of development as I thought it would be more efficient size-wise, while still being simple enough, than producing entire charts on the backend and then finding a way to send much larger data to the server to render.

This turned out to be **too complex for the scenario and not worth the runtime saved, if any**.  In addition, it was quite difficult to get anything to render properly as the JavaScript required to render the data sent didn't play well with the Jinja2 templating.  The slight formatting difference between JavaScript json and Python dictionaries as well as the need to **manually format datetime units** generated a lot of messy, unmanageable, and ineffecient code.  Even though it would require me to reconfigure the **stock_chart.py** module, I decided switching my approach entirely would be a lot more scaleable and workable than trying to force my original plan.

##### Solution: Using Plotly to Create Temporary HTML Candlestick Chart Files on the Backend

After some research, I found **Plotly** (which you can read more about [here](https://plotly.com/python/candlestick-charts/)) to be a great solution to all of my issues.  I actually didn't need to change that much of the stock_chart.py module to format the data for the library.  In terms of data-points, I just needed to provide datetimes in epoch format, which only required a dividing TDA's datetimes by 1000 to convert to seconds, and then a list of every open, high, low, and close.  A candlestick chart figure object could then be created from this data, followed by easily updating its layout to add appropriate titles and axis labels, and then using **Plotly's IO library** to write the chart to its own html file using a **special filepath** format to allow for easy creation, identification, and deletion of a chart:
<center>*frontend/graphs/graph<b>{symbol}{timeframe option (ex: "10d")}{true/false include ext hrs}</b>.html*</center>

##### Timeframe Option Buttons null due to not Loading in DOM Before Setting onClick Events

In order for the user to be able to access different time period charts, the Bootstrap card within the stock/index profile modal requires **buttons with onClick events to send a request to the server for that specific chart's html**.  The charts can be accessed from two different pages, the **Home Page** and the **Movers Page**, via either **a direct symbol lookup POST** or **by clicking a symbol link**.  I originally planned on sending these button elements with their onClick events the same way for both methods: **adding the elements and script at the same time as modal**.

Unfortunately, when accessing the chart feature after submitting a direct lookup, only a few of these buttons would load in the DOM before the events would all try to be set.  The **1d, 3d, 5d, and 10d buttons** would exist in the DOM in time, but not any of the buttons beyond that, so while setting the onClick events would work for those, it would try to assign onClick events to **null elements**, even though the buttons would load right after that.  This frustrated me for a while, as I even made sure to try including **window.onload** to solve the issue, but nothing I tried as a workaround in JavaScript seemed to have any effect.  Eventually, after overthinking the problem for a extensive amount of time, I came up with a much more straightforward and simplistic approach to this feature.

##### Solution: Add the Button Elements into the Hidden Lookup Modal as Part of the Page at Load

Adding the two groups of buttons with unique ids into the **home.html** template directly was a much easier solution.  These buttons exist in the modal that only appears after submitting a direct symbol lookup into the form on the page, so they don't take up any space on the page when navigating to it through a standard GET request.  When the form is submited, the function that adds the script to immediately load the modal **will also have the necessary JavaScript to add the onClick events** to the buttons with corresponding ids.  Since the buttons already exist in the DOM, there are no null buttons, and the events are added successfully.  Each button can now appropriately tell the server to create and load a chart's html to the modal for the user to see.

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