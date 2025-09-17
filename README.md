# **KEYLOGGER EM PYTHON**

<img src="imagens/pypic.png" alt="Yui Hirasawa" width="409">


Este projeto é um **keylogger educativo** desenvolvido em Python, com uma interface gráfica simples usando `tkinter`. Ele registra as teclas pressionadas no sistema e gera relatórios periódicos em arquivo `.txt` ou por e-mail.

> ⚠️ **Aviso Legal:** Este software foi desenvolvido exclusivamente para fins educacionais e testes em ambientes controlados. O uso indevido pode violar leis de privacidade e segurança digital. Nunca utilize este programa sem o consentimento explícito do usuário do dispositivo. É expressamente proibido utilizar este projeto para fins maliciosos, como perseguição (stalking), espionagem ou qualquer outra atividade ilegal.

---

## ✨ Funcionalidades

- Captura de teclas em tempo real com a biblioteca `keyboard`
- Interface gráfica para iniciar o monitoramento e visualizar os logs
- Relatórios automáticos a cada X segundos (configurável, você pode alterar no código o tempo)
- Opção de salvar os logs em arquivo ou enviar por e-mail
- Organização dos logs com timestamps no nome do arquivo

---

## 🛠️ Tecnologias Utilizadas

- `keyboard` – captura de eventos de teclado
- `tkinter` – interface gráfica
- `threading` – execução paralela
- `smtplib` e `email.mime` – envio e formatação de e-mails
- `datetime` – manipulação de datas e horários

---

## ⚙️ Configurações

| Parâmetro            | Descrição                                     | Valor padrão            |
| --------------------- | ----------------------------------------------- | ------------------------ |
| `SEND_REPORT_EVERY` | Intervalo entre relatórios (segundos)          | `60`                   |
| `EMAIL_ADDRESS`     | E-mail usado para envio de relatórios          | `"email@provider.tld"` |
| `EMAIL_PASSWORD`    | Senha do e-mail                                 | `"password_here"`      |
| `report_method`     | Método de relatório:`"file"` ou `"email"` | `"file"`               |

---

## 🚀 Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
