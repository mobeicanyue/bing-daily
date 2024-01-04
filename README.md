`The original purpose of this project was to act as a daily image for the blog, but with the addition of a file extension the url is directly cached by the browser and is not changed on a daily basis at all. So the alternative is to write a service to be deployed on the server that redirects the requested url 302 to the bing daily image.`

`本项目最初的目的是充当博客的每日一图，但是加上文件后缀的 url 浏览器直接缓存，根本不会每日更换。所以替代方案是写一个服务 在服务器部署，将请求的网址 302 重定向到 bing 每日一图`


Fetch Bing daily image at UTC 00:00 and store it in the release.

在北京时间 8:00 获取 Bing 每日图片并存储在 release 中。

## Usage/用法:
use as a wallpaper source
https://cdn.jsdelivr.net/gh/mobeicanyue/bing-daily@release/default.jpg


## Syntax/语法:
https://cdn.jsdelivr.net/gh/mobeicanyue/bing-daily@release/{location}-{dpi}.jpg

example:

https://cdn.jsdelivr.net/gh/mobeicanyue/bing-daily@release/en-US-1920x1080.jpg

or

https://cdn.jsdelivr.net/gh/mobeicanyue/bing-daily@release/{location}-{dpi}.webp
