function connect_hw(lang, code) {
    txta = document.querySelector('#id_answer')
    txta.focus()
    txta.is = 'highlighted-code'
    txta.theme = 'github-dark'
    txta.language = lang
    if(code) {
        txta.innerText = code
    }
}