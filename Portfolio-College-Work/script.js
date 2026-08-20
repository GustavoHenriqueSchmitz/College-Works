document.addEventListener("DOMContentLoaded", () => {
    // 1. Lógica do Menu Hambúrguer (Mobile)
    const mobileMenu = document.getElementById("mobile-menu");
    const navLinks = document.getElementById("nav-links");
    const navItems = document.querySelectorAll(".nav-links a");

    // Alterna o estado do menu ao clicar no ícone
    if (mobileMenu && navLinks) {
        mobileMenu.addEventListener("click", () => {
            mobileMenu.classList.toggle("is-active");
            navLinks.classList.toggle("active");
        });

        // Fecha o menu automaticamente ao clicar em um link
        navItems.forEach(item => {
            item.addEventListener("click", () => {
                mobileMenu.classList.remove("is-active");
                navLinks.classList.remove("active");
            });
        });
    }

    // 2. Lógica do Formulário de Contato
    const contactForm = document.getElementById("contactForm");

    // Cria um listener no formulário
    if (contactForm) {
        contactForm.addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent the default DOM submit events

            // Pega os valores do formulário
            const nome = document.getElementById("nome").value.trim();
            const email = document.getElementById("email").value.trim();
            const mensagem = document.getElementById("mensagem").value.trim();

            // Verifique se todos inputs foram preenchidos, se não pare o processo e mostra uma mensagem de erro
            if (nome === "" || email === "" || mensagem === "") {
                alert("Erro: Todos os campos (Nome, E-mail e Mensagem) devem ser preenchidos.");
                return;
            }

            // Lógica Regex para validar se o email inserido é um email válido
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert("Erro: Por favor, insira um endereço de e-mail válido.");
                return;
            }

            // Mostre uma mensagem dizendo que o processo de envio aconteceu com sucesso, e depois resete o formulário
            alert(`Mensagem enviada com sucesso!\n\nObrigado pelo contato, ${nome}.`);
            contactForm.reset();
        });
    }
});
