function conv()
{
    let x=document.getElementById("dollar")
    let k=x.value 
    let rupees=k*74.5
    let result=document.getElementById("result")
    result.textContent = k + " dollars is equal to " + rupees + " Indian Rupees.";
}