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


console.info('Hamburger! hamburger? hamburger...')