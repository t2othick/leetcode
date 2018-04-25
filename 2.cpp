struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* current;
    struct ListNode* c1 = l1;
    struct ListNode* c2 = l2;
    int carry = 0;

    head -> val = (c1 -> val + c2 -> val + carry) % 10;
    carry = (c1 -> val + c2 -> val + carry) >= 10 ? 1 : 0;
    head -> next = NULL;

    current = head;
    c1 = c1 -> next;
    c2 = c2 -> next;

    while(c1 && c2) {
        current -> next = malloc(sizeof(struct ListNode));
        current -> next -> val = (c1 -> val + c2 -> val + carry) % 10;
        current -> next -> next = NULL;
        carry = (c1 -> val + c2 -> val + carry) >= 10 ? 1 : 0;
        current = current -> next;
        c1 = c1 -> next;
        c2 = c2 -> next;
    }

    struct ListNode* extra = c1 ? c1 : c2;


    while (extra) {
        current -> next = malloc(sizeof(struct ListNode));
        current -> next -> val = (extra -> val + carry) % 10;
        current -> next -> next = NULL;
        carry = (extra -> val + carry) >= 10 ? 1 : 0;
        current = current -> next;
        extra = extra -> next;
    }


    if (carry) {
        current -> next = malloc(sizeof(struct ListNode));
        current -> next -> val = 1;
        current -> next -> next = NULL;
    }

    return head;

}
