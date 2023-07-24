const nums = [3,7,6,15];
const target = 9;

function soloution(nums,target){
    let map = new Map();

    for(let i = 0; i < nums.length; i++){
        let compliment = target - nums[i];
        if(map.has(compliment)){
            console.log( [map.get(compliment),i])
        }else{
            map.set(nums[i],i);
        }
    }

}

console.log(soloution(nums,target));

const num = [3,7,2,15]
const sum = 9;
let mapTwo = new Map()

for(let i = 0; i < num.length;i++){
    let complimentTwo = sum - num[i]
    console.log(complimentTwo)
    if(mapTwo.has(complimentTwo)){
        console.log( [i,mapTwo.get(complimentTwo)])
    }else{
        mapTwo.set(num[i],i)
    }
}