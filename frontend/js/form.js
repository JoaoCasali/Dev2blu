function salvar(event) {
    event.preventDefault();
    var listaAlunos = JSON.parse(localStorage.getItem('Funcionarios'));

    if (listaAlunos == null) {
        listaAlunos = [];
        id = 0;
    }
    else {
        var id = JSON.parse(localStorage.getItem('IdFuncionario'));
        id = id + 1;
    }

    var name = document.getElementById('nome').value;
    var doc_people = document.getElementById('cargo').value;
    var year = document.getElementById('salario').value;

    var Aluno = {
        'id': id,
        'nome': name,
        'cpf': doc_people,
        'idade': year
    }; listaAlunos.push(Aluno);


    localStorage.setItem('IdFuncionario', JSON.stringify(id));
    localStorage.setItem('Funcionarios', JSON.stringify(listaAlunos));
    document.getElementById('form').reset();
}

const form = document.getElementById('form');

form.addEventListener('submit', salvar);
