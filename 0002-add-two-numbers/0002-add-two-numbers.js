/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let new_head = new ListNode(0);
    let curr = new_head;
    let carry = 0;
    
    while (l1!= null || l2 != null || carry != 0) {
        let digit1 = l1 ? l1.val : 0;
        let digit2 = l2 ? l2.val : 0;
        
        let result = digit1 + digit2 + carry;
        carry = Math.floor(result / 10);
        console.log(carry)
        result = result % 10;
        
        let new_node = new ListNode(result);
        
        curr.next = new_node;
        curr = new_node;
        
        if(l1 != null) l1 = l1.next
        
        if(l2 != null) l2 = l2.next
    }
    
    return new_head.next
};