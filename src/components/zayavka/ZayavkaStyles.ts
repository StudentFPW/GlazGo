import styled, { css } from "styled-components";

export const Container = styled.div`
    margin: 20px 0; 
`
export const Title = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-bottom: 32px;
    position: relative;
`
export const Header = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    position: relative;
`
export const Status = styled.div`
    position: absolute;
    left: 0;
    font-size: 12px;

`
export const Close = styled.button`
    position: absolute;
    right: 0;
`
export const VacancyName = styled.div`
    text-align: center;
    margin: 4px 0 10px;
`
export const Head = styled.div`
    display: flex;
    justify-content: space-between;
    margin-bottom: 26px;
`
export const Info = styled.div`
    /* margin-bottom: 26px; */
`
export const AutoItem = styled.div`
    margin-bottom: 10px;
`
export const Form = styled.form`
    display: flex;
    flex-direction: column;
    justify-content: stretch;
    margin: 20px 0;
`
export const input = css`
    height: 40px;
    background: #F0F0F0;
    border: none;
    margin: 2px 0 14px;
    padding: 10px;
`
export const Select = styled.select`
    ${input}
`
export const Input = styled.input`
    ${input}
`
export const Buttons = styled.div`
    display: flex;
    flex-direction: column;
    row-gap: 16px;
`
