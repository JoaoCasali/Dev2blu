function editar(event) {
    event.preventDefault();

    var id = document.getElementById('id').value;
    var nome = document.getElementById('nome').value;
    var cargo = document.getElementById('cargo').value;
    var salario = document.getElementById('salario').value;

    var Aluno = {
        'id': id,
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    };

    var listaAlunos = JSON.parse(localStorage.getItem('Funcionarios'));

    novaLista = []
    listaAlunos.forEach(e => {
        if (e['id'] != id) {
            novaLista.push(e);
        }
        else {
            novaLista.push(Aluno);
        }
    });
    localStorage.setItem('Funcionarios', JSON.stringify(novaLista));
    window.location.href = "listar.html";
}

function carregaCampos(dado) {
    document.getElementById('id').value = dado['id'];
    document.getElementById('nome').value = dado['nome'];
    document.getElementById('cargo').value = dado['cargo'];
    document.getElementById('salario').value = dado['salario'];
};

function carregadados() {
    var urlParametros = new URLSearchParams(window.location.search);

    var id = parseInt = (urlParametros.get('id'));

    var funcionarios = JSON.parse(localStorage.getItem('Funcionarios'));

    funcionarios.forEach(e => {
        if (e['id'] == id) {
            carregaCampos(e);
        }
    });
};

const form = document.getElementById('form');

form.addEventListener('submit', editar);

window.onload = carregadados