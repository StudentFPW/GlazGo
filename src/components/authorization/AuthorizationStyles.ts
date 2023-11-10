import { styled } from "styled-components";

export const Form = styled.form`
    display: flex;
    flex-direction: column;
`
export const Label = styled.label`
    margin-bottom: 8px;
`
export const Input = styled.input`
    margin-bottom: 8px;
    height: 48px;
    padding: 11px 16px;
    border-radius: 8px;
`
export const Button = styled.button`
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    background-color: ${({ theme }) => theme.colors.primary};
    &&[disabled] {
        background-color: ${({ theme }) => theme.colors.inactive};
    }
`