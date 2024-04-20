<div class="row ">
	<div class="col ">
		<h1  style="color:#C6AB7C; font-size: 80px; font-weight:bold;">WEB SCRAPING CONSTRUCTION COMPANIES</h1>
	</div>
</div>

<h4 align="justify">
      In the Atlantico department - Colombia, there are many housing projects, where people of all classes can get their own home, 
      but the information is not centered  in one company, each company has its information in own website, and to see webside by website is boring. 
</h4> 
<h4 align="justify">
      Knowing that, I investigated the main companies that are developing housing projects in Atlantico and start to scrap the data like name, type, 
	description, area of apartment and ect. After that, to store that information in a Excel file to watch the information to compare  project 
	by project like datasheet. 
</h4> 
<h4 align="justify">
     This project work together with the project <a href="https://github.com/kaacuna20/Website-house-project-searching-">"Website house project searching"</a>, to get that 
      information to enable fill the database with each data project.
</h4> 

### Virtual Enviroment

`$ python -m virtualenv venv`

#### Execute virtualenv:

`$ .\venv\Scripts\activate`

### Instalation packages

* `$ pip install requests`
* `$ pip install bs4`
* `$ pip install Selenium`
* `$ pip install python-dotenv`
* `$ pip install Openpyxl`

### Goal
<p align="justify">There are many ways to get data from websites, for example with API, forms and etc. But, sometimes the information has not in a centered repository, like
      this case and get thousands of data manually is no efficient, so, the method to use was <strong>"the web scraping"</strong>, and scrap the data of interest of each website 
      by project automatically, using tools like <strong>BEAUTIFULSOUP</strong> and <strong>SELENIUM</strong>.
</p>

### Steps
<ul>
	<li>
		<p align="justify">
		     Firts, investigate the main construction company that develop housing projects in Atlantico, watch background of their websites and understand the HTML elements acording with
         interest data.
		</p>
 	</li>
	<li>
  	<p align="justify">
    		After that, create a file.py for each company, create a class with the company name, define the attributes, generally were a list with the endpoints of each individual project
        and a list_projects where a dictionary with each data scraped is being append to that list. Later, create a method where start to select the <strong>HTML element</strong> either 
        using tag_name, classes or css_selector, save it in variables like city, location, logo, etc, adding a dictionary and that dictionary was attached in the list_projects. This 
        process was repeated for each project.
  	</p>
 	</li>
	<li>
		<p align="justify">Some datas could not be scraped, even some entire projects was not posible to scrap the information due to forbidden permission, so, those projects were added
        in a file call <strong>"others.py"</strong>. Each data was achieved manually, and the list that content the dictionaries were saved in class OthersPorjects attributes, where
        each attribute has the project name.
		</p>
 	</li>
	<li>
		<p align="justify">
		      Getting projects data, with the library <strong>Openpyxl</strong>, create a file.py call <strong>"dataexcel"</strong>, import each project class, and create a file.xlsx call
          "projects", later create one sheet by project and start to write each data in its corresponding sheet automatically.
		</p>
	 </li>
	<li>
		<p align="justify">
			  Later, analizate the excel file, fill the empty cells and correct wrong fields manually. After that, using <strong> Selenium drive</strong>, start a download the logos and background
         images using their url's saved in Excel file inf file.png with the method <stron>"img.screenshot_as_png"</stron>, and storage in the folder call <strong>"static"</strong>.  
		</p>
	</li>
  <li>
		<p align="justify">
			  Finally, the most important step is to fill those data in database of project <a href="https://github.com/kaacuna20/Website-house-project-searching-">"Website house project searching"</a>
        , and its API with the method POST that let post a record by project and storage in database, so create a for Loop, using a valid apikey and create a dictionary call "Parameters", start 
        to make the post request and print the repsponse to know if each record was posted successfully or not.
		</p>
	</li>
</ul>
