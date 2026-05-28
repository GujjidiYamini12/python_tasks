document
.getElementById(
"movieSearch"
)

.addEventListener(

"keyup",

function(){

let value=

this.value
.toLowerCase();

let rows=

document.querySelectorAll(
".movie-table tr"
);

rows.forEach(

(row,index)=>{

if(index===0)
return;

let text=

row.innerText
.toLowerCase();

row.style.display=

text.includes(
value
)

?

""

:

"none";

}

);

}
);