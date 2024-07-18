<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Média de Gols por Jogo</title>
    <style>
        .info { display: none; }
        .info h2 { margin-top: 0; }
        button { margin: 5px; }
    </style>
    <script>
        // Função para exibir informações sobre um time específico
        function showInfo(time) {
            var infoDivs = document.getElementsByClassName('info');
            for (var i = 0; i < infoDivs.length; i++) {
                infoDivs[i].style.display = 'none';
            }
            document.getElementById(time).style.display = 'block';
        }

        // Função para carregar os dados JSON e gerar o HTML
        function loadJSON() {
            fetch('resultados.json')
                .then(response => response.json())
                .then(data => {
                    var resultados = data;
                    generateHTML(resultados);
                });
        }

        // Função para gerar o HTML dinamicamente a partir dos dados dos resultados
        function generateHTML(resultados) {
            var container = document.getElementById('container');
            var buttonsDiv = document.createElement('div');

            // Criar um conjunto de times para garantir que os botões sejam únicos
            var timesSet = new Set();

            // Preencher o conjunto de times
            resultados.forEach(item => {
                timesSet.add(item.Time);
            });

            // Criar botões para cada time
            timesSet.forEach(time => {
                var button = document.createElement('button');
                button.textContent = time;
                button.onclick = function() {
                    showInfo(time);
                };
                buttonsDiv.appendChild(button);
            });

            container.appendChild(buttonsDiv);

            // Criar divs com informações para cada time
            timesSet.forEach(time => {
                var infoDiv = document.createElement('div');
                infoDiv.id = time;
                infoDiv.className = 'info';

                var title = document.createElement('h2');
                title.textContent = time;
                infoDiv.appendChild(title);

                resultados.forEach(item => {
                    if (item.Time === time) {
                        var p = document.createElement('p');
                        p.textContent = 'Média de gols por partida contra ' + item.Adversário + ': ' + item['Média de Gols por Partida'] + ' (Total de jogos: ' + item['Total de Jogos'] + ')';
                        infoDiv.appendChild(p);
                    }
                });

                container.appendChild(infoDiv);
            });
        }

        // Carregar os dados JSON quando o documento estiver pronto
        window.onload = loadJSON;
    </script>
</head>
<body>
    <h1>Média de Gols por Jogo</h1>
    <div id="container"></div>
</body>
</html>
