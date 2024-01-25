type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    const total = 0
    const p =  await promise1 + await promise2;
    
    return total + p
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */