    if (!localStorage.getItem('--background-color')) {
        localStorage.setItem('--background-color', '#eee');
        localStorage.setItem('--accent', '#999');
        localStorage.setItem('--black', '#222');
        localStorage.setItem('--veryblack', '#000');
    }


    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // hello world
        document.documentElement.style.setProperty('--background-color', '#eee');
        document.documentElement.style.setProperty('--black', '#222');
        document.documentElement.style.setProperty('--veryblack', '#000');
    } else {
        localStorage.setItem('--background-color', '#111');
        localStorage.setItem('--accent', '#999');
        localStorage.setItem('--black', '#ddd');
        localStorage.setItem('--veryblack', '#fff');
        document.documentElement.style.setProperty('--background-color', localStorage.getItem('--background-color'));
        document.documentElement.style.setProperty('--black',  localStorage.getItem('--black'));
        document.documentElement.style.setProperty('--veryblack',  localStorage.getItem('--veryblack'));
    }

const ch_btn = document.querySelector('.ch-theme-btn')



ch_btn.addEventListener('click', () => {
    if (localStorage.getItem('--background-color') == '#eee'){

        

        localStorage.setItem('--background-color', '#111');
        localStorage.setItem('--accent', '#999');
        localStorage.setItem('--black', '#fff');
        localStorage.setItem('--veryblack', '#fff');
        console.log('#111')
        document.documentElement.style.setProperty('--background-color', localStorage.getItem('--background-color'));
        document.documentElement.style.setProperty('--black',  localStorage.getItem('--black'));
        document.documentElement.style.setProperty('--veryblack',   localStorage.getItem('--veryblack'));
        

    }
    else {

        localStorage.setItem('--background-color', '#eee');
        localStorage.setItem('--accent', '#999');
        localStorage.setItem('--black', '#222');
        localStorage.setItem('--veryblack', '#000');
        console.log('#eee')
        document.documentElement.style.setProperty('--background-color', localStorage.getItem('--background-color'));
        document.documentElement.style.setProperty('--black',  localStorage.getItem('--black'));
        document.documentElement.style.setProperty('--veryblack', localStorage.getItem('--veryblack'));
    }

})