# relink
Automatically change links to outdated website directories

__Rationale__
* Oftentimes we will come across a webpage with a list of resources. They could be for learning Python, or a list of Italian pasta recipes. However, the site may have not been managed/updated recently, and one of the links could be outdated. Can we write a program that will update the link?

__Questions to ask__
* How does someone invoke this program?
* Within what bounds will it function? (Within a webpage? Site? Domain?)
* How will it find the updated link?
* What language or API would be best for this?
* Should it be run as a script? Software? JavaScript module?

__What it needs to do__
* Identify an outdated link
* Find the page from the link

```ex. recipes.com/alfredo_sauce```
* Update old link

__What I propose__
* Program identifies link
* Program tests link

```It's determined viable if it lands on a webpage and unviable it it hits some sort of error page or home page (because sometimes a non-existant page will redirect to a homepage)```
* If viable then move on
* If unviable then use hints in URL to search for and locate new page

```for example the people at recipes.com has changed their site layout so that there is a sub-directory for sauces. *recipes.com/alfredo_sauce* is now *recipes.com/sauces/alfredo_sauce*```

```perhaps we could parse the URL and search web indexes for "recipes.com", "alfredo", and "sauce" to find the new URL. Is there a more stable way to do this?```
* Use located URL to update old link
