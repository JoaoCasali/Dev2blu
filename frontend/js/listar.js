function deletar(id) {
    var funcionarios = JSON.parse(localStorage.getItem('Funcionarios'));
    var novalista = [];
    funcionarios.forEach(e => {
        if (e['id'] != id) {
            novalista.push(e)
        }
    });
    localStorage.setItem('Funcionarios', JSON.stringify(novalista));
    listar();
}

function listar() {
    var tbody = document.querySelector('tbody');
    tbody.innerHTML = ''

    var funcionarios = localStorage.getItem('Funcionarios');

    funcionarios = JSON.parse(funcionarios);

    if (funcionarios == null) {
        var tr = `<tr><td colspan="5" style="color: black">Não há nenhum funcionário</td></tr>`
        tbody.innerHTML = tr;
        return;
    }

    funcionarios.forEach((e) => {
        var tr = `<tr>
                    <td>${e['id']}</td>
                    <td>${e['nome']}</td>
                    <td>${e['cargo']}</td>
                    <td>${e['salario']}</td>
                    <td>
                        <a href="editar.html?id=${e['id']}">editar</a>
                        <a onclick="deletar(${e['id']})">Deletar</a>
                    </td>
                </tr>`;

        tbody.innerHTML += tr;
    }
    );
}

window.onload = listar