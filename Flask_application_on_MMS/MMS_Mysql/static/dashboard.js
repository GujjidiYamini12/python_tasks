new Chart(

document.getElementById(
"movieChart"
),

{

type:"bar",

data:{

labels:[

"Movies",

"Users",

"Theaters",

"Shows"

],

datasets:[{

data:[

movieCount,

userCount,

theaterCount,

showCount

]

}]

}

}

);