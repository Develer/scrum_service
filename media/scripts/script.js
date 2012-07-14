function MyFunc()
{
    var myVariable = "Hello world!";
    for (count=1; count<10; count++)
    {
        myVariable = myVariable + count
    }
    alert(myVariable);
}

function Greet()
{
    alert("Hi!");
    var name = "";
    do {
        name = prompt("Put your name", "");
        alert(name);
    } while (confirm("Repeat?"));
}

function While_me()
{
    var d = 5;
    var f = 1;
    for (i=1; i<=d; i++)
    f=f*i;
    alert(f);
}

function ChangeElement(element)
{
    document.getElementById(element).style.backgroundColor = '#ffc068';
}

function showAlert()
{
    if (document.getElementById('paragraph-2').style.color == 'black')
    {
        document.getElementById('paragraph-2').style.color = '#ffbb00';
        document.getElementById('paragraph-2').style.backgroundColor = 'black';
    }
    else
    {
        document.getElementById('paragraph-2').style.color = 'black';
        document.getElementById('paragraph-2').style.backgroundColor = '#ffbb00';
    }
}