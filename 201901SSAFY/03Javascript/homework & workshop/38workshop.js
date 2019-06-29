const waitNSeconds = (n) => new Promise((resolve, reject) => {
    if (typeof n !== 'number') {
        reject(n)
    }
    setTimeout(() => {
        console.log(`${n} second(s) passed`)
        resolve()
    }, n * 1000)
    
}) 

  
const waitFor10Seconds = async () => {
    await waitNSeconds(1)
    await waitNSeconds(2)
    await waitNSeconds(3)
    await waitNSeconds(4)
    console.log('Total 10 seconds!')
}

waitFor10Seconds()