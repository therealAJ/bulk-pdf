<p align="center">
  <img src="/media/bull.png"/>
  <br>
  <br>
  <b>Bulk PDF downloader</b>
  <br>
  <i>* will only work for local and non-hosted PDF's *</i>
  
  <a><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a><img src="https://img.shields.io/badge/python-3.5%2C%203.6-39CCCC.svg"></a>
</p>

> a cli for downloading external pdf's (for lazy people like me)

<br>

![Alt text](https://raw.githubusercontent.com/therealAJ/bulk-pdf/master/media/demo.gif)

<br>

## Motivation
One day I was downloading what felt like millions of PDF packages of CS notes. A couple minutes in, I got really tired of right clicking `Save Link As`. So I decided to build this :)   


## Requirements 

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
$ python pdf.py <URL-CONTAINING-DESIRED-PDFS> <dest/which/you/want/to/download/to>
```

Downloads discovered PDFs to specified `path`.

<br>

For example:

```sh
$ python pdf.py https://www.cs.ubc.ca/~schmidtm/Courses/340-F16/ ~/Desktop/Lectures
# downloads all PDFs to your `~/Desktop/Lectures` folder
