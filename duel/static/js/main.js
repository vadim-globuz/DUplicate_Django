function time() {
    setTimeout(alert, 3000)
}
time()
const name = document.querySelector('.name')
name.addEventListener('click', e => {
    name.style.color = 'blue'
})