# TD Ameritrade Full-Stack Web App Demo: <br>*A Flask Web App with a Bootstrap Frontend Built on TD Ameritrade's (TDA) Stock Market Developer APIs*
<h3>
Web App Link Here: <a href="linkhere.com">Deployed on Heroku</a><br>
Developed by Jason Schneider | <i>Contact Me At: jasondukeschneider@gmail.com</i>
</h3>

<h4><u>IMPORTANT NOTICES:</u></h4>
* **Heroku's free tier for web hosting will automatically put to sleep any free site/app after 30 minutes of inactivity, so the app may take around 10 seconds to initially wake and load if you are the first to navigate to the link in a while.**
* **The API Key visible in the bd_config.py file is intentionally visible for code review purposes (so you can get an idea as to what one may look like) *as it was only active during development and has since been deactivated and replaced by a new API Key on the Heroku repository*.**


## Quick Links
* **App Features, Use, and Demonstration Video:** [Link](https://videolinkplaceholder.com)
* **My LinkedIn:** [Link](https://www.linkedin.com/in/jason-schneider-772a19173/)
* TD Ameritrade Developer APIs and Documentation: [Link](https://developer.tdameritrade.com/apis)
* TD Ameritrade Symbol Lookup (Used in Implementation): [Link](https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp)
* Flask Web Framework: [Link](https://flask.palletsprojects.com/en/1.1.x/)
* Bootstrap 4 Documentation: [Link](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Table of Contents
* ["FAQs" For Interested Employers, Recruiters, and Organizations](#faqs-for-interested-employers-recruiters-and-organizations)
	* [What languages and technologies were used?](#what-languages-and-technologies-were-used)
	* [What was the purpose of this web app project?](#what-was-the-purpose-of-this-web-app-project)
	* [What are the main features the web app demo?](#what-are-the-main-features-the-web-app-demo)
		* [All Pages](#all-pages)
		* [Home Page](#home-page)
		* [Options Page](#options-page)
		* [Movers Page](#movers-page)
	* [What challenges did I face and how did I overcome them or deal with them?](#what-challenges-did-i-face-and-how-did-i-overcome-them-or-deal-with-them)
		* [COVID-19 Pandemic](#covid19-Pandemic)
		* [Unexpected TDA Options Chain API Parameter/Filter Interaction](#unexpected-tda-options-chain-api-parameterfilter-interaction)
		* [Webscraping TD Ameritrade's Symbol Lookup Results for App's "Search By Name" Feature](#webscraping-td-ameritrades-symbol-lookup-results-for-app's-search-by-name-feature)
		* [Candlestick Chart Rendering and Timeframe Option Button onClick Events](#candlestick-chart-rendering-and-timeframe-option-button-onclick-events)
	* [What did I learn and/or gain from this experience?
](#what-did-i-learn-andor-gain-from-this-experience)
* [TD Ameritrade Developer APIs](#td-ameritrade-developer-apis)
* [Backend Modules and Functions](#backend-modules-and-functions)
* [Framework and Hosting](#framework-and-hosting)
* [Frontend and UI/UX](#frontend-and-uiux)

## "FAQs" For Interested Employers, Recruiters, and Organizations

### What languages and technologies were used?
**Data API**: TD Ameritrade's Developer APIs *(app licensed under my personal account)*<br>
**Backend**: *Python 3.7.3* with the main libraries being *Pandas, Requests, Plotly, and Datetime*<br>
**Framework**: *Flask Web Framework*<br>
**Frontend/UI**: Plain *JavaScript*, *jQuery*, and *HTML/CSS (using Bootstrap 4)*

### What was the purpose of this web app project?

The purpose of this project was to be a **personal side project** that refreshed, sharpened, and further developed my skills in **full-stack development** (as well as the languages and tools used in the project individually) during a pandemic that interrupted my original post-graduation plans.  Given that we had, and still have, no idea how much longer this pandemic might last, I wanted to work on a practical side project for an **hour or two every day on average** *(in a corporate or professional development environment, I would obviously have worked on something like this for around eight hours a day or so, and therefore, would've finished it much more quickly)* so that I could use my time during the pandemic productively and **gain more experience, knowledge, and insight** as a full-stack developer.

This project was also a great opportunity to learn more about a personal interest of mine: **the stock market.**  I eventually plan to develop a predictive model for personal investments down the line, and this project was able to give me experience with APIs I likely want to use as well as **methods of handling, processing, and understanding raw stock market data**.  My involvement with this project will serve as invaluable resource and reference when I do decide to develop that for myself, after further research and experience of course.

### What are the main features the web app demo?

#### All Pages
* **Optimized for desktop and laptop screens** but fully functional and accessible across all devices, screen sizes, and browsers (TODO: make sure to double check older IE)
* **Bootstrap CSS Styling** across all pages for minimal, modern, and aesthetic feel
* **Card-Based Sectioning** allows for intuitive background coloring and clean sectioning of information
* **Responsive Navbar** with hamburger button and dropdown menu for smaller screens

#### Home Page

* **"Market At A Glance..."** cards that shows automatically updating market information for the **Dow Jones Industrial Average**, **S&P 500**, and **NASDAQ Composite**
* **Stock/Index Direct Lookup By Symbol**
* **Stock/Index Search By Name** with a results table of up to 50 entries and smart redirection to a direct match
	* **Direct Profile Links** in the results table open a symbol's profile modal with one click
* **Stock/Index Quote & Profile Bootstrap Modal** containing quotes, interactive candlestick charts with the ability to show different time periods, and various information about the symbol

#### Options Page
* **Options Chain Lookup for Any Optionable Symbol** that loads in Bootstrap modal
* **Intuitive Collapsable Card Accordian Option Chain Display** grouped by expiration date with number of contracts per date shown
* **Support for Several Filters to Specify Desired Option Chains**:
	* *Contract Type, Max # of Strikes, Exact Strike, Range, Expiration Range, Expiration Month, and Standard/Non-Standard Contracts...*
	* *OR enter a symbol and search with default settings right away!*

#### Movers Page
* **Top 10 Movers** for the **Dow Jones Industrial Average**, **S&P 500**, and **NASDAQ Composite**
* **Movers Tables Quickly Toggalable by Change in % and $** by preloading both types of tables for both directions of each index
* **Quick Direct Profile Links** on the symbol and name of every movers table entry to **open its profile modal** right from the Movers page

### What challenges did I face and how did I overcome them or deal with them?

#### COVID-19 Pandemic
The largest problem I faced wasn't an issue with code, development, or a bug: it was the **COVID-19 Pandemic**.  The pandemic has hit everyone hard and differently, whether we or a loved one has actually contracted it or not.  While I have been fortunate so far as to not contract it myself, the pandemic has certainly **impacted my mental health**, and also has had me quite worried about family members and relatives who are at risk.  While the manner in which it has affected these things is a private matter, it definitely had the largest burden on this project out of any of the challenges I faced.  Despite the difficulty the situation posed for me, I saw this project idea as an **opportunity to not only recover from the impacts of the pandemic, but also to grow as a developer** due to the less-than-desired conditions that can frequently come up during development on a larger scale.  I was able to push through this adveristy with **dedication and persistance** to **achieve the purposes and goals I set** for this project and present it to anyone who may be interested.

#### Unexpected TDA Options Chain API Parameter/Filter Interaction
The next largest issue I faced was **undocumented and unexpected functionality when requesting TD Ameritrade's Option Chains API** that I needed to handle on my end to **fulfill expected and desired implementation and functionality**.  You can read more about this specific API [here](https://developer.tdameritrade.com/option-chains/apis/get/marketdata/chains).

##### _Brief Summary of the API, Examples of Proper Functionality, and the Unexpected Functionality_

The Options Chain API takes a variety of parameters in its query string: some optional, some with defaults, and only one parameter that is required for proper functionality, which is the **symbol** (need to know which symbol to get an option chain for).  Many of these parameters are designed and intended to work at the same time to filter results to certain criteria, however, **some cannot be combined or else the API will respond with useless results, no results or an error**.

An example of two parameters that **can and should be combined** (aside from symbol and any other parameter) are **contractType** *(calls, puts, or calls & puts)* and **expMonth** *(only show an options expiring in this month)*.  This functions **as expected**: if I wanted **only calls expiring in March** for a certain symbol, the request would respond with a JSON with **options contracts that are calls expiring in March** *(which could be no results, if there aren't any contracts for this symbol expiring in March)*

An example of some parameters that **can't and should not be combined** are **fromDate and toDate** *(only get options contracts expiring between these dates)* and then a completely different **expMonth**.  Since these **both specify a time period of valid options contracts**, the time periods will almost always **conflict** and therefore **should not be combined**.  While they technically can be combined from the API's perspective, this doesn't make any sense when using the API as a data source, so the **app UI disables the Expiration Month field if a date is entered into the Expriations From/To Date and vice versa**.

The functionality issue arose when combining **numContracts** *(renamed to <b>numStrikes</b> in code and UI as this parameter actually specifies the number of strike prices returned, with each strike price having one or two associated contracts depending on contractType setting)* and **range** *(in/out/near-the-money, strikes-at/below/near-market, or all possible contracts)*.  If a **range value other than ALL, SAK, SBK, or SNK** is sent to the API, the value of **numContracts is completely ignored** and the **response will be the exact same regardless of what numContracts value it is given**.  This is not the functionality that is expected and takes away a control feature I want the user to have.  Since I can't edit the API source code, I came up with a different solution.

##### _Solution: the trulyApplyFilters function_

Aside from disabling incompatible parameter combinations via javaScript, I created a function that *manually applies* **numContracts <i>(aka numStrikes)</i>** after allowing the API to apply the **range** first that takes the following parameters:

```python
def trulyApplyFilters(info, numStrikes, rng):
```

The first parameter, **info**, is a dictionary containing the underlying price of a certain symbol, and then either a dataframe for calls or a dataframe for puts, or a dataframe for both.  **numStrikes** and **rng** *(stands for range, since range is a keyword in python already)* are passed from the parent function it is used in, but are the exact same values inputted by the user in the UI.  The code in this function will only run if the range value is **ITM, OTM, or NTM** and **numStrikes is not an empty string**.  If these conditions are met, it will loop through the dataframe(s) in info manually and **drop any rows** representing contracts within the same expiration date group that **exceed the max numStrikes provided**.  It then re-indexes the dataframes to ensure that they will still display properly in the Option Chain Modal.  You can learn more about how this is done specifically by looking at the source code in the repository.

#### Webscraping TD Ameritrade's Symbol Lookup Results for App's "Search By Name" Feature

In order to include the **"Search By Name"** feature on the home page that generates a table of matches with a symbol that links straight to their quote & information profile, I needed to find a data source that could support this feature.  Unfortunately, TD Ameritrade **does not offer an API that can fulfill this feature**.  In order to ensure that new stocks and indicies that come into existence during development and after release, I decided to use TD Ameritrade's [**Symbol Lookup Website**](https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp).

##### _Webscraping the Symbol Lookup Results Table for Web App Use_

I used **[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** along with the **[lxml](https://lxml.de/index.html#documentation)** parser, my two favorite webscraping libraries during my time at the University of Maryland and in other side projects, to handle processing the website results.  I was able to do this by sending a GET request to the symbol lookup website with a query parameter of **text=<i>searchValue</i>**, and then searching for the specific table element I wanted.  Getting the results and formatting them into a table with a link on the symbol that was found to link that allows the user **bring up its profile modal from whichever page they're on**.  However, the results generated by the website **only shows a maximum of 50 results per page when sending a request**.

After searching on the symbol lookup website by name, TD Ameritrade will paginate the extra results with links that will load the next page's results.  It also will show options to show more than 50 per page.  **Due to the way that TD Ameritrade has implemented their website <i>(and for understandable reasons, given that this is their data and they want to make sure it is used in ways that is acceptable to them)</i>, it isn't possible to access these extra pages' links nor is it possible to parse the page generated by a POST request that tries to select the maximum number of results per page**.  I tried this with different parses and several different approaches to be able to access these extra results through code, but their website simply prevented this from being possible.

##### _Solution: Only Show Limited Results_

Since this web app is a demo and not a full-fledged enterprise application, I figured the best solution here would be to simply provide the user with a maximum of the first 50 results for any name search they perform.  **In most cases, 50 results is plenty:** *a large majority of the first 50 results tend to be extremely obscure indicies with very long symbols that don't have any practical use*.  While I had hoped to find a way to access all possible results, the extra data being retrieved and processed would increase load times for very little practicality, since any useful name matches are typically in the top 10 results.  **Despite this, if I had a better data source or higher specification standards from a client/manager, I would absolutely find a way to implement this feature as planned**.

#### Candlestick Chart Rendering and Timeframe Option Button onClick Events

Displaying **price history candlestick charts** for a symbol to the user as well as allowing them to **select a timeframe option** *(for example, displaying a price history chart for TSLA over the past 3 months)*, something most stock market websites and applications provide, was a key feature that needed to be included and created some troublesome issues.

##### _Chart Processing, Creation, and Rendering_

**Originally** I planned on sending a dictionary/json to the flask server containing all necessary format settings, information, and price history data, and then using **canvas.js** to create and render this chart on the frontend when necessary.  I had planned on handling this feature in this way throughout a decent portion of development as I thought it would be more efficient size-wise, while still being simple enough, than producing entire charts on the backend and then finding a way to send much larger data to the server to render.

This turned out to be **too complex for the scenario and not worth the runtime saved, if any**.  In addition, it was quite difficult to get anything to render properly as the JavaScript required to render the data sent didn't play well with the Jinja2 templating.  The slight formatting difference between JavaScript json and Python dictionaries as well as the need to **manually format datetime units** generated a lot of messy, unmanageable, and ineffecient code.  Even though it would require me to reconfigure the **stock_chart.py** module, I decided switching my approach entirely would be a lot more scaleable and workable than trying to force my original plan.

##### _Solution: Using Plotly to Create Temporary HTML Candlestick Chart Files on the Backend_

After some research, I found **Plotly** (which you can read more about [here](https://plotly.com/python/candlestick-charts/)) to be a great solution to all of my issues.  I actually didn't need to change that much of the stock_chart.py module to format the data for the library.  In terms of data-points, I just needed to provide datetimes in epoch format, which only required a dividing TDA's datetimes by 1000 to convert to seconds, and then a list of every open, high, low, and close.  A candlestick chart figure object could then be created from this data, followed by easily updating its layout to add appropriate titles and axis labels, and then using **Plotly's IO library** to write the chart to its own html file using a **special filepath** format to allow for easy creation, identification, and deletion of a chart:
	
	frontend/graphs/graph{symbol}{timeframe option}{true/false include exthrs}.html

##### _Timeframe Option Buttons null due to not Loading in DOM Before Setting onClick Events_

In order for the user to be able to access different time period charts, the Bootstrap card within the stock/index profile modal requires **buttons with onClick events to send a request to the server for that specific chart's html**.  The charts can be accessed from two different pages, the **Home Page** and the **Movers Page**, via either **a direct symbol lookup POST** or **by clicking a symbol link**.  I originally planned on sending these button elements with their onClick events the same way for both methods: **adding the elements and script at the same time as modal**.

Unfortunately, when accessing the chart feature after submitting a direct lookup, only a few of these buttons would load in the DOM before the events would all try to be set.  The **1d, 3d, 5d, and 10d buttons** would exist in the DOM in time, but not any of the buttons beyond that, so while setting the onClick events would work for those, it would try to assign onClick events to **null elements**, even though the buttons would load right after that.  This frustrated me for a while, as I even made sure to try including **window.onload** to solve the issue, but nothing I tried as a workaround in JavaScript seemed to have any effect.  Eventually, after overthinking the problem for a extensive amount of time, I came up with a much more straightforward and simplistic approach to this feature.

##### _Solution: Add the Button Elements into the Hidden Lookup Modal as Part of the Page at Load_

Adding the two groups of buttons with unique ids into the **home.html** template directly was a much easier solution.  These buttons exist in the modal that only appears after submitting a direct symbol lookup into the form on the page, so they don't take up any space on the page when navigating to it through a standard GET request.  When the form is submited, the function that adds the script to immediately load the modal **will also have the necessary JavaScript to add the onClick events** to the buttons with corresponding ids.  Since the buttons already exist in the DOM, there are no null buttons, and the events are added successfully.  Each button can now appropriately tell the server to create and load a chart's html to the modal for the user to see.

### What did I learn and/or gain from this experience?
While I have had a decent amount of experience in full-stack development through my time at the University of Maryland, and more recently and importantly, my internship at **Eagle Technologies** where I was the **lead full-stack developer on the then new SAMHSA Play 2 Documentation Site Application**, this project furthered my knowledge about developing full-stack applications.  I gained a much better perspective on how long certain things take as a single developer working with new frameworks and APIs, with one big determination being that things almost always tend to take longer than expected, especially if they are to be done well.  Since this was a personal side project, I didn't exactly have any hard deadlines or specific timeline expectations, so **I was able to experience how long something would take compared to *how long I thought it would*.**  Going forward, certain things that might've taken me much longer than expected will **take far less time the next time I encounter them**, even if the technologies are different, since the concepts behind them are mostly the same.

As stated earlier, this is the first time I've used the **Flask Web Framework** specifically, and also the first time I've deployed an app to a **web host accessible from anywhere**, unlike in-house test deployment environments or using a "localhost server" (such as XAMPP in college).  It was an amazing feeling to see my project come together piece by piece and then eventually become a website I could open on my mom's computer.  Those final couple steps were really only a theoretical process to me before or something handled by other employees.

Working on this project also further advanced skills required of me as a developer regardless of what specific type of development I may be tasked with.  Working more with **Python**, even though it is my most-used and favorite language, still uncovered some tricks and knowledge that I didn't have before.  I was able to further refine my ability to **write documentation** that is easily **readable and accessible** as well as utilize **github** to make sure my git skills were refreshed and used to keep quality versioning and progress documented and backed up.

## TD Ameritrade Developer APIs
Explanation Here
## Backend Modules and Functions
Documentation Here
## Framework and Hosting
More Documentation Here
## Frontend and UI/UX
More Documentation Here