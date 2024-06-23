function connect_hw(lang, code) {
    txta = document.querySelector('#id_answer')
    txta.focus()
    txta.is = 'highlighted-code'
    txta.theme = 'github-dark'
    txta.language = lang
    if(code) {
        txta.innerHTML = code.replace(/!!change_str_webbox_hm!!/g, '')
        console.log(txta.innerHTML)
    }
}