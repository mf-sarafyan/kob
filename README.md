
# Como brincar

## Me manda seu usuário do git
Me manda seu usuário do git que eu tenho que te adicionar como colaborador pra vc poder puxar o repo

## Clona o repo pra sua máquina
- Baixa o git https://git-scm.com/downloads e faz as parada pra instalar
- Configura os treco dele (segue tutorial etc)
- Clona o repo -> vai numa pasta com o git bash e roda `git clone https://github.com/mf-sarafyan/kob.git`

## Setup do obsidian
Cria uma vault no obsidian na pasta que vc clonou 
Pra renderizar os links bonitinhos precisa instalar no obsidian o plugin **dataview** (vai em community plugins e instala)

**Melhor jeito de ver o grafo:**
```
- Abre o graph view
- Coloca um filtro-> path:"kob/content/1 Keepers' Compendium/wiki"  
- Cria Groups, cada um de uma cor:
	- ["type":"character"]
	- ["type":"location"]
	- ["type":"faction"]
	- ["type":"entry"]
```

## Facilidades q eu coloquei
Tem 2 codiguinhos na root do projeto:
- `publish-branch.bat` -> vc roda esse e ele vai subir suas mudanças numa branch nova
	- daí vc pode ir no github criar uma PR pra eu atualizar a main 
- `pull.bat` -> esse muda pra branch main e atualiza com as últimas mudanças. pode dar merda se vc tiver mudanças em aberto, então antes de dar pull, manda o publish-branch. MAS antes de fazer qqr coisa é bom dar pull, sempre que abrir, pra ter certeza q tá atualizado 

### Facilitando as facilidades
Dá pra colocar hotkey no obsidian pra rodar esses 2 codiguinho e facilitar a vida mais. 
- Instala o plugin `shell commands`
- Vai nas configs dele
- Cria comandinhos `cd kob && publish-branch.bat` e `cd kob && pull.bat` 
- Clica lá pra adicionar hotkey
Pronto, vc tem botões pra dar pull e push. Eu uso ctrl+alt+shift+enter pra push e ctrl+alt+shift+tab pra pull
