function salvar(event) {
    event.preventDefault();
    var listaFuncionarios = JSON.parse(localStorage.getItem('Funcionarios'));

    if (listaFuncionarios == null) {
        listaFuncionarios = [];
        id = 0;
    }
    else {
        var id = JSON.parse(localStorage.getItem('IdFuncionario'));
        id = id + 1;
    }

    var nome = document.getElementById('nome').value;
    var cargo = document.getElementById('cargo').value;
    var salario = document.getElementById('salario').value;

    var funcionario = {
        'id': id,
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    }; listaFuncionarios.push(funcionario);


    localStorage.setItem('IdFuncionario', JSON.stringify(id));
    localStorage.setItem('Funcionarios', JSON.stringify(listaFuncionarios));
    document.getElementById('form').reset();
}

const form = document.getElementById('form');

form.addEventListener('submit', salvar);
