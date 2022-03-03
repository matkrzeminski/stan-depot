const URL = document.URL

const navItems = document.querySelectorAll('.nav-item')

for (const item of navItems) {
  if(URL === item.href) {
    item.classList.add('active')
  }
}
