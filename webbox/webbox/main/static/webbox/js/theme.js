// :root {
//     --background-color: #eee;
//     --accent: #f09e8c;
//     --black: #7b8937;
//     --card-bg-color: #6b7436;
//     --nigga: black;
//     --text-color: #f4d9c1;
//     --link-color: #111;
//     --btn-color: #f4d9c1;
//     --btn-background-color: #d72f01;
//     --not-very-important: #ad2702;
//     --important: #d72f01;
// }


// localStorage.setItem('--background-color', '#eee');
// localStorage.setItem('--accent', '#999');
// localStorage.setItem('--black', '#222');
// localStorage.setItem('--veryblack', '#000');



    
    
    if (!localStorage.getItem('--background-color')) {
        localStorage.setItem('--background-color', '#eee');
        localStorage.setItem('--accent', '#f09e8c');
        localStorage.setItem('--black', '#7b8937');
        localStorage.setItem('--card-bg-color', '#6b7436');
        localStorage.setItem('--nigga', 'black');
        localStorage.setItem('--text-color', '#f4d9c1');
        localStorage.setItem('--link-color', '#111');
        localStorage.setItem('--btn-color', '#f4d9c1');
        localStorage.setItem('--btn-background-color', '#d72f01');
        localStorage.setItem('--not-very-important', '#ad2702');
        localStorage.setItem('--important', '#d72f01');

    }


    // if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    //     // hello world
    //     document.documentElement.style.setProperty('--background-color', '#eee');
    //     document.documentElement.style.setProperty('--black', '#222');
    //     document.documentElement.style.setProperty('--veryblack', '#000');
    // } else {
    //     localStorage.setItem('--background-color', '#111');
    //     localStorage.setItem('--accent', '#999');
    //     localStorage.setItem('--black', '#ddd');
    //     localStorage.setItem('--veryblack', '#fff');
    //     document.documentElement.style.setProperty('--background-color', localStorage.getItem('--background-color'));
    //     document.documentElement.style.setProperty('--black',  localStorage.getItem('--black'));
    //     document.documentElement.style.setProperty('--veryblack',  localStorage.getItem('--veryblack'));
    // }

const ch_btn = document.querySelector('.ch-theme-btn')



ch_btn.addEventListener('click', () => {
    if (!(localStorage.getItem('--background-color') == '#eee')){

        

        localStorage.setItem('--background-color', '#eee');
        localStorage.setItem('--accent', '#f09e8c');
        localStorage.setItem('--black', '#7b8937');
        localStorage.setItem('--card-bg-color', '#6b7436');
        localStorage.setItem('--nigga', 'black');
        localStorage.setItem('--text-color', '#f4d9c1');
        localStorage.setItem('--link-color', '#111');
        localStorage.setItem('--btn-color', '#f4d9c1');
        localStorage.setItem('--btn-background-color', '#d72f01');
        localStorage.setItem('--not-very-important', '#ad2702');
        localStorage.setItem('--important', '#d72f01');
        console.log('#111')
        document.documentElement.style.setProperty('--background-color', localStorage.getItem('--background-color'));
        document.documentElement.style.setProperty('--black',  localStorage.getItem('--black'));
        document.documentElement.style.setProperty('--accent',   localStorage.getItem('--accent'));
        document.documentElement.style.setProperty('--card-bg-color',   localStorage.getItem('--card-bg-color'));
        document.documentElement.style.setProperty('--nigga',   localStorage.getItem('--nigga'));
        document.documentElement.style.setProperty('--text-color',   localStorage.getItem('--text-color'));
        document.documentElement.style.setProperty('--link-color',   localStorage.getItem('--link-color'));
        document.documentElement.style.setProperty('--btn-color',   localStorage.getItem('--btn-color'));
        document.documentElement.style.setProperty('--btn-background-color',   localStorage.getItem('--btn-background-color'));
        document.documentElement.style.setProperty('--not-very-important',   localStorage.getItem('--not-very-important'));
        document.documentElement.style.setProperty('--important',   localStorage.getItem('--important'));


        
        

    }
    else {

        localStorage.setItem('--background-color', '#eed');
        localStorage.setItem('--accent', '#999');
        localStorage.setItem('--black', '#222');
        localStorage.setItem('--card-bg-color', '#222');
        localStorage.setItem('--nigga', '#222');
        localStorage.setItem('--text-color', '#eed');
        localStorage.setItem('--link-color', '#eed');
        localStorage.setItem('--btn-color', '#eed');
        localStorage.setItem('--btn-background-color', '#222');
        localStorage.setItem('--not-very-important', '#ad2702');
        localStorage.setItem('--important', '#d72f01');
        console.log('#111')
        document.documentElement.style.setProperty('--background-color', localStorage.getItem('--background-color'));
        document.documentElement.style.setProperty('--black',  localStorage.getItem('--black'));
        document.documentElement.style.setProperty('--accent',   localStorage.getItem('--accent'));
        document.documentElement.style.setProperty('--card-bg-color',   localStorage.getItem('--card-bg-color'));
        document.documentElement.style.setProperty('--nigga',   localStorage.getItem('--nigga'));
        document.documentElement.style.setProperty('--text-color',   localStorage.getItem('--text-color'));
        document.documentElement.style.setProperty('--link-color',   localStorage.getItem('--link-color'));
        document.documentElement.style.setProperty('--btn-color',   localStorage.getItem('--btn-color'));
        document.documentElement.style.setProperty('--btn-background-color',   localStorage.getItem('--btn-background-color'));
        document.documentElement.style.setProperty('--not-very-important',   localStorage.getItem('--not-very-important'));
        document.documentElement.style.setProperty('--important',   localStorage.getItem('--important'));
    }

    TRANSITION = localStorage.getItem('--black')

})