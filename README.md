<h3 font-size='20px' align='center'>Bulk PDF downloader</h3>
<p align="center">
  <img src="/media/bull.png"/>
  <br>
  <br>
  <i>* will with work for local and non-hosted PDF's *</i>
  
  <a><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a><img src="https://img.shields.io/badge/python-3.5%2C%203.6-39CCCC.svg"></a>
</p>

> a cli for downloading external pdf's (for lazy people like me)

<br>

## Demo

![Alt text](https://raw.githubusercontent.com/therealAJ/bulk-pdf/master/media/demo.gif)

<br>

## Motivation
One day I was downloading what felt like millions of PDF packages of CS notes. A couple minutes in, I got really tired of right clicking `Save Link As`. So I decided to build this :)   


## Requirements

`argparse`
<br>
`urllib`
<br>
`requests`
<br>
`wget`
<br>
`python >= 3.5`

## Install

```sh
$ git clone https://github.com/therealAJ/bulk-pdf
$ cd bulk-pdf
$ pip install -r reqs.txt
```

## Usage

```sh
$ python pdf.py <URL-CONTAINING-DESIRED-PDFS> <dest/which/you/want/to/download/to> [OPTIONAL-BASE-URL-FOR-HOSTED-PDFS]
```

Downloads discovered PDFs to specified `path`.

<br>

For example:

```sh
$ python pdf.py https://www.cs.ubc.ca/~schmidtm/Courses/340-F16/ ~/Desktop/Lectures
# downloads all PDFs to your `~/Desktop/Lectures` folder
```

### Notes

Webpages have different ways of hosting PDFs, some use an absolute url, like `https://hosting-site.com/hello.pdf`, others host locally and have `href` tags looking something like `\courses\cs101\hello.pdf`. The second case is the reason I added the ability to give the optional url for the parent hosting site. 
<br>
<br>
You may run into a url that looks like `https://site.com/lectures.html`. More often than not, this is where you want to use the full url to parse the entire webpage and then use `https://site.com` as the optional parameter to do the `wget` requests with. 

So, an example would look like: 
```sh
$ python pdf.py https://site.com/lectures.html ~/Desktop/Test https://site.com
```
<br>
<br>
Hopefully I haven't confused you :) File an issue if you run into anything of interest. PRs welcome :) 
