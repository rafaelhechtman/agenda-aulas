<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Média de Gols por Jogo</title>
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

            // Criar botões para cada time
            for (var time in resultados) {
                var button = document.createElement('button');
                button.textContent = time;
                button.onclick = (function(time) {
                    return function() {
                        showInfo(time);
                    };
                })(time);
                buttonsDiv.appendChild(button);
            }

            container.appendChild(buttonsDiv);

            // Criar divs com informações para cada time
            for (var time in resultados) {
                var infoDiv = document.createElement('div');
                infoDiv.id = time;
                infoDiv.className = 'info';
                infoDiv.style.display = 'none';

                var title = document.createElement('h2');
                title.textContent = time;
                infoDiv.appendChild(title);

                var results = resultados[time];
                for (var i = 0; i < results.length; i++) {
                    var p = document.createElement('p');
                    p.textContent = 'Média de gols por partida contra ' + results[i][0] + ': ' + results[i][1].toFixed(2) + ' (Total de jogos: ' + results[i][2] + ')';
                    infoDiv.appendChild(p);
                }

                container.appendChild(infoDiv);
            }
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
