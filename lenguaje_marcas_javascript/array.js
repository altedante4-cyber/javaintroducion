let arrayNuevo = [5,4,8]
document.writeln(arrayNuevo + "<br>")
arrayNuevo.push(24)
document.writeln(arrayNuevo + "<br>")
arrayNuevo.unshift(1)
document.writeln(arrayNuevo + "<br>")
arrayNuevo[3] = 10 ; 
document.writeln(arrayNuevo + "<br>")

for(const  item of arrayNuevo){
    document.writeln(item + ",")
}

document.writeln("<br>")

arrayNuevo.forEach(elemento => { // para cada elemento queiro que hatgas los isguiente 
    
    document.writeln(elemento*5);
})
document.writeln("<br>")
