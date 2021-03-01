# TD Ameritrade Full-Stack Web App Demo: <br>*A Flask Web App with a Bootstrap Frontend Built on TD Ameritrade's (TDA) Stock Market Developer APIs*
<h3>
Web App Deployed on Heroku: <a href="linkhere.com">v1.0-Production</a><br>
(Initial Deployment v1.0-Production on Date Here)<br>
Developed by Jason Schneider <br>
<i>Contact Me (for bug reports, professional opportunities, etc.): jasondukeschneider@gmail.com</i>
</h3>

#### _IMPORTANT NOTICES:_
* **Heroku's free tier for web hosting will automatically put to sleep any free site/app after 30 minutes of inactivity, so the app may take around 15-20 seconds to initially wake and load if you are the first to navigate to the link in a while.  This is a result of the hosting service and not the app or its code.**

* **The API Key in the bd_config.py file is intentionally visible for code review purposes (so you can get an idea as to what one may look like) *as it was only active during development and has since been deactivated and replaced by a new API Key on the Heroku repository*.**


## Quick Links
* [***App Features, Use, and Demonstration Video***](https://videolinkplaceholder.com)
* [**My LinkedIn**](https://www.linkedin.com/in/jason-schneider-772a19173/)
* [TD Ameritrade Developer APIs and Documentation](https://developer.tdameritrade.com/apis)
* [TD Ameritrade Symbol Lookup](https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp)
* [Flask Web Framework](https://flask.palletsprojects.com/en/1.1.x/)
* [Bootstrap 4 Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Table of Contents
* ["FAQs" For Interested Employers, Recruiters, and Organizations](#faqs-for-interested-employers-recruiters-and-organizations)
	* [What languages and technologies were used?](#what-languages-and-technologies-were-used)
	* [What was the purpose of this web app project?](#what-was-the-purpose-of-this-web-app-project)
	* [What are the main features the web app demo?](#what-are-the-main-features-the-web-app-demo)
		* [All Pages](#all-pages)
		* [Home Page](#home-page)
		* [Options Page](#options-page)
		* [Movers Page](#movers-page)
		* [Potential for Future Development](#potential-for-future-development)
	* [What challenges did I face and how did I overcome them or deal with them?](#what-challenges-did-i-face-and-how-did-i-overcome-them-or-deal-with-them)
		* [COVID-19 Pandemic](#covid19-Pandemic)
		* [Unexpected TDA Options Chain API Parameter/Filter Interaction](#unexpected-tda-options-chain-api-parameterfilter-interaction)
		* [Webscraping TD Ameritrade's Symbol Lookup Results for App's "Search By Name" Feature](#webscraping-td-ameritrades-symbol-lookup-results-for-apps-search-by-name-feature)
		* [Candlestick Chart Rendering and Timeframe Option Button onClick Events](#candlestick-chart-rendering-and-timeframe-option-button-onclick-events)
	* [What did I learn and/or gain from this experience?
](#what-did-i-learn-andor-gain-from-this-experience)
* [TD Ameritrade Developer APIs](#td-ameritrade-developer-apis)
	* [Introduction and Reasons Of Use](#introduction-and-reasons-of-use)
	* [Get Quote](#get-quote-documentation)
	* [Get Price History](#get-price-history-documentation)
	* [Get Option Chain](#get-option-chain-documentation)
	* [Get Movers](#get-movers-documentation)
* [Backend Modules and Functions](#backend-modules-and-functions)
	* [stock_info.py](#stock_infopy)
		* [getBySymbol(sym, symType = "")](#getbysymbolsym-symtype--)
		* [getByName(name)](#getbynamename)
	* [stock_chart.py](#stock_chartpy)
		* [createChart(sym, time = "10d", hasExtHrs = True)](#createchartsym-time--10d-hasexthrs--true)
	* [stock_options.py](#stock_optionspy)
		* [getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo, expMonth, standard)](#getoptionchainsym-contype-numstrikes-strike-rng-expfrom-expto-expmonth-standard)
		* [trulyApplyFilters(info, numStrikes, rng) (Called Within getOptionChain)](#trulyapplyfiltersinfo-numstrikes-rng-called-within-getoptionchain)
	* [stock_movers.py](#stock_moverspy)
		* [getMovers(index, direction, change)](#getmoversindex-direction-change)
	* [stock_aux.py](#stock_auxpy)
		* [attrFormat(sym, attr, value)](#attrformatsym-attr-value)
* [Framework, Frontend, and UI](#framework-frontend-and-ui)

## "FAQs" For Interested Employers, Recruiters, and Organizations

### What languages and technologies were used?
**Data API**: TD Ameritrade's Developer APIs *(app licensed under my personal account)*<br>
**Backend**: *Python 3.7.3* with the main libraries being *Pandas, Requests, Plotly, and Datetime*<br>
**Framework**: *Flask Web Framework*<br>
**Frontend/UI**: Plain *JavaScript*, *jQuery*, and *HTML/CSS (using Bootstrap 4)*

### What was the purpose of this web app project?

The purpose of this project was to be a **personal side project** that refreshed, sharpened, and further developed my skills in **full-stack development** (as well as the languages and tools used in the project individually) during a pandemic that interrupted my original post-graduation plans.  Given that we had, and still have, no idea how much longer this pandemic might last, I wanted to work on a practical side project for about an **hour per day on average** *(in a corporate or professional development environment, I would have worked on something like this for around eight hours a day or so, and therefore, would've undoubtedly finished it much less time)* so that I could use my time during the pandemic productively and **gain more experience, knowledge, and insight** as a full-stack developer.

This project was also a great opportunity to learn more about a personal interest of mine: **the stock market.**  I eventually plan to develop a predictive model for personal investments down the line, and this project was able to give me experience with APIs I likely want to use as well as **methods of handling, processing, and understanding raw stock market data**.  My involvement with this project will serve as invaluable resource and reference when I do decide to develop that for myself, after further research and experience of course.

### What are the main features the web app demo?

#### All Pages
* **Optimized for desktop and laptop screens** but fully functional and accessible across all devices, screen sizes, and browsers
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

#### Potential for Future Development
* **Templated UI Design** allows for easy addition, removal, or changing of elements
* **Demo Includes Extra Backend Data for Possible Future Development** allows for easy addition of feature expansion, feature inclusion, and scalability *(such as inclusion of last price in movers backend, full options name in options backend, etc. for demonstrating potential for additions)*

### What challenges did I face and how did I overcome them or deal with them?

#### COVID-19 Pandemic
The largest problem I faced wasn't an issue with code, development, or a bug: it was the **COVID-19 Pandemic**.  The pandemic has hit everyone hard and differently, whether we or a loved one has actually contracted it or not.  While I have been fortunate so far as to not contract it myself, the pandemic has certainly **impacted my mental health**, and also has had me quite worried about family members and relatives who are at risk.  While the manner in which it has affected these things is a private matter, it definitely had the largest burden on this project out of any of the challenges I faced.  Despite the difficulty the situation posed for me, I saw this project idea as an **opportunity to not only recover from the impacts of the pandemic, but also to grow as a developer** due to the less-than-desired conditions that can frequently come up during development on a larger scale.  I was able to push through this adveristy with **dedication and persistance** to **achieve the purposes and goals I set** for this project and present it to anyone who may be interested.

#### Unexpected TDA Options Chain API Parameter/Filter Interaction
The next largest issue I faced was **undocumented and unexpected functionality when requesting TD Ameritrade's Option Chains API** that I needed to handle on my end to **fulfill expected and desired implementation and functionality**.  You can read more about this specific API [here](https://developer.tdameritrade.com/option-chains/apis/get/marketdata/chains).

##### _Brief Summary of the API, Examples of Proper Functionality, and the Unexpected Functionality_

The Options Chain API takes a variety of parameters in its query string: some optional, some with defaults, and only one parameter that is required for proper functionality, which is the **symbol** (need to know which symbol to get an option chain for).  Many of these parameters are designed and intended to work at the same time to filter results to certain criteria, however, **some cannot be combined or else the API will respond with useless results, no results or an error**.

An example of two parameters that **can and should be combined** (aside from symbol and any other parameter) are **contractType** *(calls, puts, or calls & puts)* and **expMonth** *(only show an options expiring in this month)*.  This functions **as expected**: if I wanted **only calls expiring in March** for a certain symbol, the request would respond with a JSON with **options contracts that are calls expiring in March** *(which could be no results, if there aren't any contracts for this symbol expiring in March)*

An example of some parameters that **can't and should not be combined** are **fromDate and toDate** *(only get options contracts expiring between these dates)* and then a completely different **expMonth**.  Since these **both specify a time period of valid options contracts**, the time periods will almost always **conflict** and therefore **should not be combined**.  While they technically can be combined from the API's perspective, this doesn't make any sense when using the API as a data source, so the **app UI disables the Expiration Month field if a date is entered into the Expriations From/To Date and vice versa**.

The functionality issue arose when combining **numContracts** *(renamed to <b>numStrikes</b> in code and UI as this parameter actually specifies the number of strike prices returned, with each strike price having one or two associated contracts depending on contractType setting)* and **range** *(in/out/near-the-money or all possible contracts)*.  If a **range value other than ALL, SAK, SNK, or SBK** *(SAK, SNK, and SBK are unsupported by the app as I noticed late in development that they apparently did nothing regardless of what other values were and were not set despite earlier preliminary testing, even changing between them with the exact same settings did nothing to alter any results whatsoever)* is sent to the API, the value of **numContracts is completely ignored** and the **response will be the exact same regardless of what numContracts value it is given**.  This is not the functionality that is expected and takes away a control feature I want the user to have.  Since I can't edit the API source code, I came up with a different solution.

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
	
	frontend/charts/chart{symbol}{timeframe option}{true/false include exthrs}.html

##### _Timeframe Option Buttons null due to not Loading in DOM Before Setting onClick Events_

In order for the user to be able to access different time period charts, the Bootstrap card within the stock/index profile modal requires **buttons with onClick events to send a request to the server for that specific chart's html**.  The charts can be accessed from two different pages, the **Home Page** and the **Movers Page**, via either **a direct symbol lookup POST** or **by clicking a symbol link**.  I originally planned on sending these button elements with their onClick events the same way for both methods: **adding the elements and script at the same time as modal**.

Unfortunately, when accessing the chart feature after submitting a direct lookup, only a few of these buttons would load in the DOM before the events would all try to be set.  The **1d, 3d, 5d, and 10d buttons** would exist in the DOM in time, but not any of the buttons beyond that, so while setting the onClick events would work for those, it would try to assign onClick events to **null elements**, even though the buttons would load right after that.  This frustrated me for a while, as I even made sure to try including **window.onload** to solve the issue, but nothing I tried as a workaround in JavaScript seemed to have any effect.  Eventually, after overthinking the problem for a extensive amount of time, I came up with a much more straightforward and simplistic approach to this feature.

##### _Solution: Add the Button Elements into the Hidden Lookup Modal as Part of the Page at Load_

Adding the two groups of buttons with unique ids into the **home.html** template directly was a much easier solution.  These buttons exist in the modal that only appears after submitting a direct symbol lookup into the form on the page, so they don't take up any space on the page when navigating to it through a standard GET request.  When the form is submited, the function that adds the script to immediately load the modal **will also have the necessary JavaScript to add the onClick events** to the buttons with corresponding ids.  Since the buttons already exist in the DOM, there are no null buttons, and the events are added successfully.  Each button can now appropriately tell the server to create and load a chart's html to the modal for the user to see.

### What did I learn and/or gain from this experience?
While I have had a decent amount of experience in full-stack development through my time at the University of Maryland, and more recently and importantly, my internship at **Eagle Technologies** where I was the **lead full-stack developer on the then new SAMHSA Play 2 Documentation Site Application**, this project furthered my knowledge about developing full-stack applications.  I gained a much better perspective on how long certain things take as a single developer working with new frameworks and APIs, with one big determination being that things almost always tend to take longer than expected, especially if they are to be done well.  Since this was a personal side project, I didn't exactly have any hard deadlines or specific timeline expectations, so **I was able to experience how long something would take compared to *how long I thought it would*.**  Going forward, certain things that might've taken me much longer than expected will **take far less time the next time I encounter them**, even if the technologies are different, since the concepts behind them are mostly the same.  

In addition, many times throughout development **I would deem something as complete and move on** to the next step, stage, function, module, etc. only to **later discover an issue, flaw, or bug and have to backtrack and fix not only the issue itself but several other files and features that were operating off a faulty feature.**  While I try to make sure I only move on when I've implemented something completely correctly, there will always be issues that pop up when you least expect them, and it is important not to let these things you from your goals.  When these issues did pop up, I was able to practice **productively channeling my frustration into fixing the issues** and **learning from the mistakes I made for the sake of future projects**.

As stated earlier, this is the first time I've used the **Flask Web Framework** specifically, and also the first time I've deployed an app to a **web host accessible from anywhere**, unlike in-house test deployment environments or using a "localhost server" (such as XAMPP in college).  It was an amazing feeling to see my project come together piece by piece and then eventually become a website I could open on my mom's computer.  Those final couple steps were really only a theoretical process to me before or something handled by other employees.

Working on this project also further advanced skills required of me as a developer regardless of what specific type of development I may be tasked with.  Working more with **Python**, even though it is my most-used and favorite language, still uncovered some tricks and knowledge that I didn't have before.  I was able to further refine my ability to **write documentation** that is easily **readable and accessible** as well as utilize **Github** to make sure my git skills were refreshed and used to keep quality versioning and progress documented and backed up.

## TD Ameritrade Developer APIs

### Introduction and Reasons Of Use

**TD Ameritrade (now operating as a subsidiary of Charles Schwab)** is the online broker and platform provide I use for my personal trades and investments.  After several months of stock market trading, my interest in a potential stock market evaluation project began to grow, so I started to look for potential APIs to use for stock data.  I found that TD Ameritrade provided their own **developer APIs that were free for personal, non-profit use as long as you register an application after making a developer account**.  Given that I already had a lot of experience with the data and services offered by their trading platform, I decided it would be a great idea to use their APIs in a project and eventually the idea for a full-stack web app that provided stock market features **using some of their GET APIs** as a data source came to fruition.

**[Their collection of APIs](https://developer.tdameritrade.com/apis)** is quite robust and is separated into many sub-categories using various http request methods.  Some of their APIs **can even automate senstive, advanced operations** with a valid authentication token, such as retrieval and changing of **account information**, **placing and changing orders**, and accessing **transaction history**.  For the purposes of this project, only GET APIs that didn't require any sensitive account credentials or advanced authorization were needed.  To implement the features desired, the APIs selected and used are described below:

### Get Quote ([Documentation](https://developer.tdameritrade.com/quotes/apis/get/marketdata/%7Bsymbol%7D/quotes))

#### Description
The **Get Quote API** gets a quote for a symbol.  The response is more than just a simple price or point value and actually returns a lot of useful data.  The exact information returned depends on the type of symbol, which can be one of the following: **mutual fund**, **future**, **future option**, **index** *(prefaced with a "\$" in TDA's APIs, even though typically it is the other way around in most investing contexts)*, **option**, **forex**, **ETF**, or **equity**.  The web app deems **anything that is not an index is a "stock"**.  The only query parameter required for this API is the api key as the symbol data is requested for is put into the resource url.

#### Use in Project
This API is used to implement the backend module **stock_info.py**, which contains two frequently used functions: `getBySymbol(sym, symType = "")` and indirectly `getByName(name)`, which calls getBySymbol in a certain case.

### Get Price History ([Documentation](https://developer.tdameritrade.com/price-history/apis/get/marketdata/%7Bsymbol%7D/pricehistory))

#### Description
The **Get Price History API** gets the price history for a symbol, which is the data needed to **render candlestick charts**.  The response is a candle list, with each candle containing a **close**, **datetime**, **high**, **low**, **open**, and **volume**.  Along with the required api key, this API takes several query parameters, with the following used in the project: **periodType**, **period**, **frequencyType**, **frequency**, and **needExtendedHoursData**.  The values these parameters can be are defined in the documentation linked above.

#### Use in Project
This API is used to implement the backend module **stock_chart.py**, which contains the chart creation function: `createChart(sym, time = "10d", hasExtHrs = True)`.

### Get Option Chain ([Documentation](https://developer.tdameritrade.com/option-chains/apis/get/marketdata/chains))

#### Description
The **Get Option Chain API** gets an option chain for an optionable symbol.  The response contains a lot of data in a complex format, much of which is unneeded for this app's functionality.  The main data that is needed from the response is the **underlying** and then the **callExpDateMap**, the **putExpDateMap**, or **both**.  Each of the maps contain another complex json list format but it will essentially **group individual options contracts by expiration date**.  Along with the api key, this API takes several query parameters, with the following used in the project: **symbol**, **contractType**, **strikeCount**, **strike**, **range**, **fromDate**, **toDate**, **expMonth**, and **optionType**.  To get a better idea of the parameters and response format, please read the documentation above.

#### Use in Project
This API is used to implement the backend module **stock_options.py**, which contains the option chain processing and formatting function: `getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo, expMonth, standard)`.

### Get Movers ([Documentation](https://developer.tdameritrade.com/movers/apis/get/marketdata/%7Bindex%7D/movers))

#### Description
The **Get Movers API** gets the top 10 (up or down) movers by value or percent for a particular market, which the hover pop-up on the documentation site states to be either the **NASDAQ Composite**, **Dow Jones Industrial Average**, or **S&P 500**.  The response is a list of movers, with each mover containing the following values: **change**, **description** *(the name of the mover)*, **direction**, **last**, **symbol**, and **totalVolume**.  Along with the api key, this API takes two other query parameters: **direction** *(up or down)* and **change** *(value or percent)*.

#### Use in Project
This API is used to implement the backend module **stock_movers.py**, which contains the function that retrieves and formats the movers into a dataframe ready for the frontend: `getMovers(index, direction, change)`.

## Backend Modules and Functions
The backend is driven by six python modules (which can be found in the **backend directory**): **stock_info.py**, **stock_chart.py**, **stock_options.py**, **stock_movers.py**, an auxiliary module named **stock_aux.py**, and the config file named **bd_config.py**.  Below you can find descriptions of each module and the functions it contains with **explanations for each parameter taken**.  An explanation of each value of the config file is contained in the comments within the file itself.

### stock_info.py

This module utilizes the **Get Quote API** to implement most of every **Stock and Index Quote & Profile Modal** and the html generation functions to create their html formatting.  It also handles **webscraping TD Ameritrade's Symbol Lookup** website to implement searching by name, as well as directly retrieving information for a symbol that is found for a name search that results in a **direct one to one match** *(for example: searching for "Lemonade" results in a one to one match for LMND on the website, so getBySymbol("LMND") is returned directly)*.

#### `getBySymbol(sym, symType = "")`

```python
# Requests the TD Ameritrade Quotes API for the stock's attributes that will
# eventually be displayed to the user on the frontend and returns a dictionary
# with each attribute and its corresponding value.  These attributes are
# defined in the config file and the README, and depend on whether the symbol
# is for a stock, index, or for the case when this is used for Index Cards for
# the "At a Glance..." Home Page Section.
def getBySymbol(sym, symType = ""):
```

***Parameters:***

* **sym**: A symbol string for an index with preceeding "\$" *(such as \$DJI)* or for a stock with no preceeding "\$" *(such as TSLA)*.  An invalid or nonexisting symbol will result in a return value of `None`.
* **symType**: A string containing a symbol type code to tell the function what types of attributes to include in its return dictionary.  Can be one of the following values **(defaults to *""* if omitted)**:
	* *indexCard* - for markets at a glance cards
	* *indexFull* - for a symbol provided with a preceeding "\$"
	* *""* (empty string) - for any other symbol, which are deemed stock symbols

***Returns:*** A `dict` of attribute names and attribute values or `None`.

#### `getByName(name)`
```python
# Searching by stock name requires a symbol lookup on an exchange's symbol
# list via a GET Request to TD Ameritrade's symbol lookup page with
# appropriate url parameters to generate a table of all stock names containing
# name.  If there is only one table entry then this function returns the
# result of getBySymbol() with the associated symbol.  Otherwise, it will
# return a dictionary of all search results with symbol keys and stock name
# values.
def getByName(name):
```

***Parameters:***

* **name**: A string representing either a full stock or index name, name fragment, or stock symbol.  Use of a stock symbol will result in the Symbol Lookup website returning a table of one line, which tells the function to return the result of `getBySymbol(name)`, which is a `dict`.

***Returns:*** One of the following:

* `None` - no results are found for `name` on the Symbol Lookup site
* `DataFrame` - contains rows matching the results table after searching on the Symbol Lookup site
* Result of `getBySymbol(name)` - in the case of a one-to-one match

### stock_chart.py

This module utilizes the **Get Price History API** to implement the stock or index **candlestick chart** of every **Stock and Index Quote & Profile Modal**.  The candlestick chart figure creation and writing to html file is achieved using **Plotly's Graph Objects and IO Libraries**.

#### `createChart(sym, time = "10d", hasExtHrs = True)`

```python
# Requests the TD Ameritrade Price History API for a given symbol, with
# frequency and periods determined by the time option (default "10d"), and
# whether or not to include extended hours data.  This data is then used to
# generate an html file written to the /frontend/charts directory using
# plotly's io library so that it can be used to easily render a chart in a
# modal on the frontend based on the file's name.
def createChart(sym, time = "10d", hasExtHrs = True):
```

***Parameters:***

* **sym:** A symbol string for either a stock or index.
* **time:** A time option string representing the period of time (in trading days) from which to create a candlestick chart of for the given symbol *(for example: 10d means "over the last 10 trading days)*.  Can be one of the following values **(defaults to *"10d"* if omitted)**:
	* *1d* - last trading day
	* *3d* - last 3 trading days
	* *5d* - last 5 trading days
	* *10d* - last 10 trading days
	* *1m* - last trading month
	* *3m* - last 3 trading months
	* *6m* - last 6 trading months
	* *1y* - last trading year
	* *3y* - last 3 trading years
	* *5y* - last 5 trading years
	* *YTD* - last trading year to date
* **hasExtHrs**: A boolean value that will include extended hours price history data if True, otherwise, only standard market hours price history data will be used (**defaults to *True* if omitted)**

**Returns:** No value returned.

### stock_options.py

This module utilizes the **Get Options Chain API** to retireve options chain data and implement the Bootstrap card accordian-style **Options Chain Modal**.  It also is responsible for handling the manual application of combining the **numStrikes** and **range** filters.  You can read more about why manual application is necessary and how it is done [here](#unexpected-tda-options-chain-api-parameterfilter-interaction).

#### `getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo, expMonth, standard)`

```python
# Requests the TD Ameritrade Options Chain API with the given request
# parameters (streamlined to include only required parameters and optional
# parameters necessary for implementation desired) and returns a dictionary
# containing the underlying price as well as dataframes for puts and calls,
# just puts, just calls, or neither (if filters are too restrictive, resulting
# in 0 options that fit criteria).
def getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo,
                   expMonth, standard):
```

***Parameters:***

* **sym**: A symbol string for an underlying stock to retrieve an options chain for.
* **conType**: A string representing the type of contracts to be included in the options chain (OC).  Can be one of the following values:
	* *CALL* - OC will include only call contracts
	* *PUT* - OC will include only put contracts
	* *ALL* - OC will include both call and put contracts
* **numStrikes**: A string representing the maximum integer number of strike prices to include per expiration date group.  **For no maximum number of strikes, this parameter's value is *""* or *"null"*.**
* **strike**: A float string *(no preceeding \$, such as "20.21")* that specifies to only include options contacts with this exact strike price.  **For no exact strike, this parameter's value is *""* or *"null"*.**
* **rng**: A string representing the range of contracts to include in the chain.  Can be one of the following values:
	* *ITM* - In the money
	* *NTM* - Near the money
	* *OTM* - Out of the money
	* ~*SAK* - Strikes Above Market Price~ ([unsupported by app frontend](#unexpected-tda-options-chain-api-parameterfilter-interaction))
	* ~*SNK* - Strikes Near Market Price~ ([unsupported by app frontend](#unexpected-tda-options-chain-api-parameterfilter-interaction))
	* ~*SBK* - Strikes Below Market Price~ ([unsupported by app frontend](#unexpected-tda-options-chain-api-parameterfilter-interaction))
* **expFrom**: A date string of format *YYYY-MM-DD* representing the starting/earliest expiry date to be included in the chain.  **For no starting/earliest expiry date, this parameter's value is *""* or *"null"*.**
* **expTo**: A date string of format *YYYY-MM-DD* representing the ending/latest expiry date to be included in the chain.  **For no ending/latest expiry date, this parameter's value is *""* or *"null"*.**
* **expMonth**: A string containing a three letter abbreviation representing the month in which only options contracts expiring in that month should be included in the chain.  Can be one of the following values **(for no expiry month, this parameter's value is *""* or *"null"*)**:
	* *JAN* - January
	* *FEB* - February
	* *MAR* - March
	* *APR* - April
	* *MAY* - May
	* *JUN* - June
	* *JUL* - July
	* *AUG* - August
	* *SEP* - September
	* *OCT* - October
	* *NOV* - November
	* *DEC* - December
	* *ALL* - All Months
* **standard**: A string representing whether to retrieve only standard contracts, only non-standard contracts, or both.  Can be one of the following values:
	* *S* - only standard contracts (representing 100 shares of the underlying security)
	* *NS* - only non-standard contracts (representing a number other than 100 shares of the underlying security)
	* *ALL* - both standard and non-standard contracts

***Returns:*** A `dict` containing the following keys and values:

* *underlyingPrice* - value is a float string with no preceeding \$
* *dfCalls* ***or this key may not exist*** - 
	* This key will only exist if the options chain includes call options
	* If it exists, its value is a `DataFrame` with the following columns: *Expiration, Strike, Bid, Ask, Market, %Chg, Volume, Type, ITM, Name*
* *dfPuts* ***or this key may not exist*** - 
	* This key will only exist if the options chain includes put options
	* If it exists, its value is a `DataFrame` with the following columns: *Expiration, Strike, Bid, Ask, Market, %Chg, Volume, Type, ITM, Name*

#### `trulyApplyFilters(info, numStrikes, rng)` *(Called Within getOptionChain)*

```python
# This function "extends" the TD Ameritrade Option Chain API's functionality by
# implenting intended interaction between the Max # of Strikes filter in
# combination with ITM, OTM, and NTM contract ranges.  By default, TD
# Ameritrade has implemented their API to completely ignore the numStrikes
# setting if one of these ranges is selected, which is not the functionality
# intended.  Preventing the user from combining these options defeats the
# purpose of this feature, so this function implements this for the users so
# they can have this feature properly.
def trulyApplyFilters(info, numStrikes, rng):
```
***Parameters:***

* **info:** A `dict` of the same exact format as the return value of `getOptionChain` (as this function makes changes to its eventual return `dict`)
* **numStrikes:** A string representing the maximum integer number of strike prices to include per expiration date group.  **For no maximum number of strikes, this parameter's value is *""* or *"null"*.**
* **rng**: A string representing the range of contracts to include in the chain.  Can be one of the following values:
	* *ITM* - In the money
	* *NTM* - Near the money
	* *OTM* - Out of the money
	* ~*SAK* - Strikes Above Market Price~ ([unsupported by app frontend](#unexpected-tda-options-chain-api-parameterfilter-interaction))
	* ~*SNK* - Strikes Near Market Price~ ([unsupported by app frontend](#unexpected-tda-options-chain-api-parameterfilter-interaction))
	* ~*SBK* - Strikes Below Market Price~ ([unsupported by app frontend](#unexpected-tda-options-chain-api-parameterfilter-interaction))

***Returns:*** A `dict` of the same format as the info parameter with proper filtering applied if required.

### stock_movers.py

This module utilizes the **Get Movers API** to retrieve market movers and implement the **top ten up and down market movers tables** within the green and red Bootstrap cards on the Movers page.

#### `getMovers(index, direction, change)`

```python
# Requests the TD Ameritrade Movers API to retrieve mover information based on
# the given parameters as a dataframe.  Movers can be retrieved for any TD
# Ameritrade supported index in either "gainer" or "loser" direction and the
# change can be in units of value or by percentage.  Last price also retrieved.
def getMovers(index, direction, change):
```

***Parameters:***

* **index**: A string containing the index symbol of one the three API supported markets:
	* *\$DJI* - Dow Jones Industrial Average
	* *\$SPX.X* - S&P 500
	* *\$COMPX* - NASDAQ Composite
* **direction**: A string with a value of either *up* (for top gainers) or *down* (for top losers).
* **change**: A string with the unit of change to retrieve top movers by, either by *percent* or by *value*.

***Returns:*** A `DataFrame` with the columns: *symbol, change, name, last*.

### stock_aux.py

This is an **auxiliary/helper module** for any functions that serve a utility purpose and/or aren't specific enough to belong in one of the other backend modules.  It currently contains only one function but exists for easy addition of more functions in the case of future development.

#### `attrFormat(sym, attr, value)`

```python
# Formats the value of an attribute to have necessary symbols before or after
# the value, such as $ <value> for money amounts or <value> % for percentages.
# Also handles rounding and date formatting.
# This applies to any data on frontend that will use data from one of the two
# functions above.  Does not apply to movers as this requires extra formatting.
def attrFormat(sym, attr, value):
```

***Parameters***:

* **sym:** A string symbol for either a stock or index.
* **attr**: A string API attribute name from one of the attribute lists in bd_config.py
* **value**: The value of the associated attribute (various types).

***Returns***: A formatted value.

## Framework, Frontend, and UI

### Framework
This web app utilizes the [**Flask Web Framework**](https://flask.palletsprojects.com/en/1.1.x/) to handle all frontend routing, requests, and functionality.  Flask is a **micro-framework** for **Python 3.5 and above** that uses **Jinja2 Templating** and the **Werkzeug WSGI Library** to achieve its purpose while being extremely lightweight.  The framework operates all of its functionality through the **app.py** module.  To start the application, it executes the following lines of code:

```python
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True)
```

### app.py

The **app.py** module contains several functions which contain `@app.route()` decorators to bind each function to a URL.  Each function is documented below similarly to the backend functions:

#### `home()`

```python
# Renders the Home page accordingly, depending on whether a GET request is
# sent (when opening the app for the first time or navigating to the root url)
# or a POST request is sent (submitting the Stock Quote & Information Lookup
# Form).  Handles all of the various form cases and renders this information
# to the user with the modal loading functionality using the same html
# generation function as the modal loading on the Movers page.
@app.route("/", methods = ["POST", "GET"])
def home():
```

#### `showChart(sym, time, hasExtHrs)`


```python
# Creates a stock or index chart on the backend and writes the html to the file
# at the destination shown below with the given parameters: a stock or index
# symbol, a time setting string (ex. 5d, 3m, 1y, etc.), and a true or false
# value as a string for whether or not to include extended hours data.  This
# html is copied and returned as wrapped, valid html, and displayed in a modal
# using a jQuery load function.
@app.route("/chart/<sym>/<time>/<hasExtHrs>")
def showChart(sym, time, hasExtHrs):
```

#### `refreshIndexCard(strippedIndexSym)`

```python
# Provides a url destination for the server to return new Index Card html.
# Since the color of each card needs to be defined in the class of the card
# element, a new card is returned by each call to this function, which then
# replaces the old card.
@app.route("/refresh/<strippedIndexSym>")
def refreshIndexCard(strippedIndexSym):
```

#### `options()`

```python
# Renders the Options page accordingly, depending on whether a GET request is
# sent (when navigating to the Options page url directly or clicking the nav
# link) or a POST request is sent (after submitting the Options Chain form).
# Handles all of the various form cases and displays the appropriate response
# to the user, as well as handling empty and disabled fields on the server
# before sending parameters to the backend for processing and API retrieval.
@app.route("/options", methods = ["POST", "GET"])
def options():
```

#### `movers()`

```python
# Loads gainer and loser movers tables for each of the API supported indicies
# ranked by both percentage and value, displaying the ranked by percentage
# tables by default and having the ranked by value tables preloaded so a simple
# toggle button can be used to nearly instantly show the other tables for each
# card.  While this does result in slower initial page load times, it allows
# for a more seamless experience after loading instead of using jQuery load
# calls.
@app.route("/movers")
def movers():
```

#### `loadModalContent(sym)`

```python
# This function loads a Stock/Index Quote & Information Profile from a link
# on either the Home Page Search by Name Results Table or a Movers Card.  It
# also hypothetically would allow for easy implementation on other additional
# pages if they were added and required this functionality.  This allows
# profiles to be viewed within the same page they were loaded from so an
# entire new page doesn't need to be loaded.
@app.route("/modalContent/<sym>")
def loadModalContent(sym):
```