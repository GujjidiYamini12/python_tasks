document.addEventListener(

    "DOMContentLoaded",

    ()=>{

        console.log(
            "MMS MongoDB Loaded"
        );

        const cards =

        document.querySelectorAll(
            ".card"
        );

        cards.forEach(

            card=>{

                card.addEventListener(

                    "mouseenter",

                    ()=>{

                        card.style.transform=
                        "scale(1.05)";
                    }

                );

                card.addEventListener(

                    "mouseleave",

                    ()=>{

                        card.style.transform=
                        "scale(1)";
                    }

                );

            }

        );

    }

);

function confirmDelete(

    item

){

    return confirm(

        `Delete ${item}?`

    );

}