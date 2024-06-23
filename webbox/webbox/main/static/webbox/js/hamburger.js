const btn = document.querySelector('#burger-checkbox')
        const menu_item = document.querySelectorAll('.menu-item')
        let open_hamburger = false
        btn.addEventListener('click', () => {
            if (open_hamburger) {
                
                document.body.style.overflow = 'auto'
            }
            else {
                document.body.style.overflow = 'hidden'
            }
            open_hamburger = !open_hamburger
        })
        for (let item in menu_item){
            try {
                menu_item[item].addEventListener('click', ()=>{
                    open_hamburger = false;
                    btn.checked = false;
                    document.body.style.overflow = 'auto'
                })
            }
            catch (TypeError) {}
            
        }


console.info('%cHamburger! hamburger? hamburger...', 'font-size: 1.5em; color: yellow; font-weight: bold; background-color: black;')