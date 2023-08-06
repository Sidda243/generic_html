
let result=document.querySelector('#one')
let a = Number(prompt('enter value of a'))
let b = Number(prompt('enter value of b'))
console.log(a,b)

function add()
{
	let Addition = a+b 
	result.innerText=Addition
}
function sub()
{
	let Subtraction = a-b 
	result.innerText=Subtraction
}
function mul()
{
	let Multiplication = a*b 
	result.innerText=Multiplication
}
function div()
{
	let Division = a%b 
    result.innerText=Division
}